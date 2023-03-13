from fastapi import APIRouter

from .endpoints import uploadfile

router = APIRouter()
router.include_router(uploadfile.router, tags=["Uploadfile"], prefix="/uploadfile")