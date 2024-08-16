from fastapi import APIRouter, Depends, Query, Request, Response
from fastapi.responses import RedirectResponse
from fief_client import FiefAccessTokenInfo

from config import AUTH_REDIRECT, SESSION_COOKIE_NAME
from utils import fief_auth
from utils.auth import fief

router = APIRouter(tags=["Auth"])


@router.get(
    "/access-info", name="获取 Access Token 信息", response_model=FiefAccessTokenInfo
)
async def get_user_info(
    access_token_info: FiefAccessTokenInfo = Depends(fief_auth.authenticated()),
):
    return access_token_info


@router.get("/callback", name="OAuth Callback")
async def auth_callback(request: Request, response: Response, code: str = Query()):
    tokens, _ = await fief.auth_callback(code, str(request.url_for("OAuth Callback")))

    response = RedirectResponse(AUTH_REDIRECT)
    response.set_cookie(
        SESSION_COOKIE_NAME,
        tokens["access_token"],
        max_age=tokens["expires_in"],
        secure=False,
        httponly=True,
    )

    return response
