from typing import Annotated

from bson.errors import InvalidId
from fastapi import APIRouter, Body, Depends, HTTPException
from fief_client import FiefAccessTokenInfo
from odmantic import AIOEngine, ObjectId

from models import Section, Staff
from utils import fief_auth
from utils.database import get_database

router = APIRouter(tags=["Staff"])


@router.post(
    "/bind-me",
    name="将当前用户和员工绑定（没有则自动创建）",
    response_model=Staff,
    dependencies=[
        Depends(fief_auth.authenticated(permissions=["oa:staff:bind"])),
    ],
)
async def bind_me(
    name: Annotated[str, Body()],
    section_id: Annotated[str, Body()],
    token_info: FiefAccessTokenInfo = Depends(fief_auth.authenticated()),
    engine: AIOEngine = Depends(get_database),
):
    async with engine.session() as session:
        result = await session.count(Staff, Staff.user_id == str(token_info["id"]))

        if result > 0:
            raise HTTPException(status_code=409, detail="该用户已经绑定了员工")

        try:
            section = await session.find_one(
                Section, Section.id == ObjectId(section_id)
            )
        except InvalidId:
            raise HTTPException(status_code=404, detail="找不到部门")

        if section is None:
            raise HTTPException(status_code=404, detail="找不到部门")

        await session.save(
            Staff(
                id=ObjectId(),
                name=name,
                tags=[],
                user_id=str(token_info["id"]),
                section=section,
            )
        )

        return await session.find_one(Staff, Staff.user_id == str(token_info["id"]))


@router.get(
    "/me",
    name="获取当前登录用户的员工信息",
    response_model=Staff,
    responses={404: {"description": "找不到员工"}},
)
async def get_me(
    token_info: FiefAccessTokenInfo = Depends(fief_auth.authenticated()),
    engine: AIOEngine = Depends(get_database),
):
    result = await engine.find_one(Staff, Staff.user_id == str(token_info["id"]))
    if result is None:
        raise HTTPException(status_code=404, detail="找不到员工")
    return result
