from fastapi import APIRouter
from database import speakers

speaker_router = APIRouter()


@speaker_router.get("/", status_code=200)
def get_speakers():
    return speakers

