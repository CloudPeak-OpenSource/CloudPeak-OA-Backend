from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from config import DATABASE_URL
from routers import auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.engine = AIOEngine(AsyncIOMotorClient(DATABASE_URL))
    yield


app = FastAPI(
    title="CloudPeak OA Backend",
    license_info={
        "name": "LGPL-3.0",
        "url": "https://www.gnu.org/licenses/lgpl-3.0.zh-cn.html",
    },
)

app.include_router(auth.router, prefix="/auth")
