from fastapi import HTTPException, Request, Response
from fastapi.security import APIKeyCookie, APIKeyHeader, OAuth2AuthorizationCodeBearer
from fief_client import FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from config import (
    FIEF_AUTHORIZATION_URL,
    FIEF_BASEURL,
    FIEF_CLIENT_ID,
    FIEF_CLIENT_SECRET,
    FIEF_TOKEN_URL,
    SESSION_COOKIE_NAME,
)

fief = FiefAsync(
    FIEF_BASEURL,
    FIEF_CLIENT_ID,
    FIEF_CLIENT_SECRET,
)


class CustomFiefAuth(FiefAuth):
    client: FiefAsync

    async def get_unauthorized_response(self, request: Request, response: Response):
        redirect_uri = request.url_for("OAuth Callback")
        auth_url = await self.client.auth_url(
            str(redirect_uri), scope=["openid", "offline_access"]
        )

        raise HTTPException(
            status_code=307,
            headers={"Location": str(auth_url)},
        )


# scheme = OAuth2AuthorizationCodeBearer(
#     FIEF_AUTHORIZATION_URL,
#     FIEF_TOKEN_URL,
#     scopes={"openid": "openid", "offline_access": "offline_access"},
#     auto_error=False,
# )

scheme = APIKeyHeader(
    name=SESSION_COOKIE_NAME,
    auto_error=False,
)

fief_auth = CustomFiefAuth(fief, scheme)

__all__ = ["fief", "fief_auth", "scheme"]
