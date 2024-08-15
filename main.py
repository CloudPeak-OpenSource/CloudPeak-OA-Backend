from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from config import DATABASE_NAME, DATABASE_URL
from routers import auth, section, staff


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(DATABASE_URL)
    app.db_engine = AIOEngine(client, database=DATABASE_NAME)

    yield

    client.close()


app = FastAPI(
    title="CloudPeak OA Backend",
    license_info={
        "name": "LGPL-3.0",
        "url": "https://www.gnu.org/licenses/lgpl-3.0.zh-cn.html",
    },
    lifespan=lifespan,
)

app.include_router(auth.router, prefix="/auth")
app.include_router(staff.router, prefix="/staff")
app.include_router(section.router, prefix="/section")
