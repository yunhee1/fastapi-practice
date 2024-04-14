from fastapi import APIRouter

user_router = router = APIRouter()

@router.get("/uni")
async def uni():
    return {"username":"윤희"}