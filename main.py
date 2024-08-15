from fastapi import FastAPI

from routers import auth

app = FastAPI(
    title="CloudPeak OA Backend",
    license_info={
        "name": "LGPL-3.0",
        "url": "https://www.gnu.org/licenses/lgpl-3.0.zh-cn.html",
    },
)

app.include_router(auth.router, prefix="/auth")
