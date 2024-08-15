from fastapi import APIRouter, Depends
from fief_client import FiefAccessTokenInfo

from utils import fief_auth

router = APIRouter(tags=["Auth"])


@router.get(
    "/access-info", name="获取 Access Token 信息", response_model=FiefAccessTokenInfo
)
async def get_user_info(
    access_token_info: FiefAccessTokenInfo = Depends(fief_auth.authenticated()),
):
    return access_token_info
