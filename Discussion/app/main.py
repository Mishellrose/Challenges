
from fastapi import FastAPI

from app.routers import adminlogin
from .routers import post,user,vote,comment,admin,auth,adminlogin
from app import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)  
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(comment.router)
app.include_router(admin.router)
app.include_router(adminlogin.router)