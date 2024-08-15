from fastapi import Request
from odmantic import AIOEngine


def get_database(request: Request) -> AIOEngine:
    return request.app.db_engine
