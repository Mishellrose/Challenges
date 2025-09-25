from .database import engine
from fastapi import FastAPI
from app.routers import post,user,vote,comment,admin
from app import models



models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)  
app.include_router(vote.router)
app.include_router(comment.router)
app.include_router(admin.router)