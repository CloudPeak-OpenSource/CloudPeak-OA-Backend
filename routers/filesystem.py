import secrets
import urllib.parse

import gridfs
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from odmantic.bson import ObjectId

from utils.database import get_gridfs

router = APIRouter(tags=["Filesystem"])


@router.get("/file", name="下载文件", response_class=StreamingResponse)
async def download_file(
    fid: ObjectId, fs: AsyncIOMotorGridFSBucket = Depends(get_gridfs)
):
    fp = await fs.open_download_stream(fid)

    async def iterfile():
        while True:
            data = await fp.read(1024 * 8)

            if not data:
                break

            yield data

    return StreamingResponse(
        iterfile(),
        media_type=(
            fp.metadata.get("media_type", "text/plain")
            if fp.metadata is not None
            else "text/plain"
        ),
        headers={
            "Content-Disposition": f'attachment; filename="{urllib.parse.quote(fp.filename if fp.filename else secrets.token_hex(16))}"'
        },
    )


@router.post(
    "/upload",
    name="上传文件",
)
async def upload_file(
    file: UploadFile = File(description="上传文件"),
    fs: AsyncIOMotorGridFSBucket = Depends(get_gridfs),
):
    async with fs.open_upload_stream(
        file.filename if file.filename else secrets.token_hex(16),
        chunk_size_bytes=256,
        metadata={"media_type": file.content_type},
    ) as f:
        while True:
            fp = await file.read(1024 * 8)
            if not fp:
                break

            await f.write(fp)

        return {"fid": str(f._id)}


@router.put("/update", name="更新文件")
async def update_file(
    fid: ObjectId,
    file: UploadFile = File(description="上传文件"),
    fs: AsyncIOMotorGridFSBucket = Depends(get_gridfs),
):
    try:
        await fs.delete(fid)
    except gridfs.NoFile:
        raise HTTPException(status_code=404, detail="找不到文件")

    async with fs.open_upload_stream_with_id(
        fid,
        file.filename if file.filename else secrets.token_hex(16),
        chunk_size_bytes=256,
        metadata={"media_type": file.content_type},
    ) as f:
        while True:
            fp = await file.read(1024 * 8)
            if not fp:
                break

            await f.write(fp)

        return {"fid": str(f._id)}


@router.delete(
    "/delete",
    name="删除文件",
    responses={
        200: {"description": "ok", "content": {"application/json": {"status": "ok"}}}
    },
)
async def delete_file(
    fid: ObjectId, fs: AsyncIOMotorGridFSBucket = Depends(get_gridfs)
):
    try:
        await fs.delete(fid)
    except gridfs.NoFile:
        raise HTTPException(status_code=404, detail="找不到文件")

    return {"status": "ok"}
