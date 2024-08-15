from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from config import (
    FIEF_AUTHORIZATION_URL,
    FIEF_BASEURL,
    FIEF_CLIENT_ID,
    FIEF_CLIENT_SECRET,
    FIEF_TOKEN_URL,
)

fief = FiefAsync(
    FIEF_BASEURL,
    FIEF_CLIENT_ID,
    FIEF_CLIENT_SECRET,
)

scheme = OAuth2AuthorizationCodeBearer(
    FIEF_AUTHORIZATION_URL,
    FIEF_TOKEN_URL,
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

fief_auth = FiefAuth(fief, scheme)

__all__ = ["fief", "fief_auth", "scheme"]
