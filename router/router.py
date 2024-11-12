from fastapi import APIRouter

from service import service

router = APIRouter()

@router.post("/summarize/")
async def summarize_video(url: str = ""):
    return service.summarize(url)