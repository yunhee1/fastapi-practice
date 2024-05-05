from fastapi import APIRouter

username_router = router = APIRouter()

@router.get("/{nickname}")
async def router3(nickname:str):
    return {"message":f"닉네임은 {nickname}입니다."}
