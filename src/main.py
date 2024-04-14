from fastapi import FastAPI
from src.routers.user import user_router
from src.routers.post import post_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(post_router, prefix="/post")

@app.get("/")
async def root():
    return {"message":"Hello World"}