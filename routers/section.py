from typing import Annotated, Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fief_client import FiefAccessTokenInfo
from odmantic import AIOEngine, ObjectId

from models import Section
from utils import fief_auth
from utils.database import get_database

router = APIRouter(tags=["Section"])


@router.get(
    "/",
    name="获取所有部门列表",
    description="需要权限 `oa:section:list`。",
    dependencies=[Depends(fief_auth.authenticated(permissions=["oa:section:list"]))],
    response_model=list[Section],
)
async def get_all_sections(engine: AIOEngine = Depends(get_database)):
    return await engine.find(Section)


@router.post(
    "/",
    name="创建部门",
    description="需要权限 `oa:section:create`。",
    dependencies=[Depends(fief_auth.authenticated(permissions=["oa:section:create"]))],
    response_model=Section,
)
async def create_section(section: Section, engine: AIOEngine = Depends(get_database)):
    return await engine.save(section)


@router.put(
    "/",
    name="更新部门",
    description="注意：部门 id 不允许更新，需要权限 `oa:section:update`。",
    dependencies=[Depends(fief_auth.authenticated(permissions=["oa:section:update"]))],
    response_model=Section,
)
async def update_section(
    section_id: ObjectId,
    patch: Annotated[dict[str, Any], Body()],
    engine: AIOEngine = Depends(get_database),
):
    section = await engine.find_one(Section, Section.id == section_id)

    if section is None:
        raise HTTPException(status_code=404, detail="找不到部门")

    section.model_update(patch, exclude={"_id", "id"})
    return await engine.save(section)


@router.delete(
    "/",
    name="删除部门",
    description="需要权限 `oa:section:delete`。",
    dependencies=[Depends(fief_auth.authenticated(permissions=["oa:section:delete"]))],
    responses={
        200: {
            "description": "部门已被删除",
            "content": {"application/json": {"example": {"status": "ok"}}},
        },
    },
)
async def delete_section(
    section_id: ObjectId, engine: AIOEngine = Depends(get_database)
):
    section = await engine.find_one(Section, Section.id == section_id)

    if section is None:
        raise HTTPException(status_code=404, detail="找不到部门")

    await engine.delete(section)

    return {"status": "ok"}
