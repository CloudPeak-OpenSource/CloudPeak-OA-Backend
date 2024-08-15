from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from odmantic import AIOEngine


def get_database(request: Request) -> AIOEngine:
    return request.app.db_engine


def get_gridfs(request: Request) -> AsyncIOMotorGridFSBucket:
    return request.app.db_gridfs
