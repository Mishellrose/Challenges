from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class PostBase(BaseModel):
    title: str
    content: str
    # tags later

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    # tags later

class AllPostsOut(BaseModel):
    posts: List[PostResponse]
    owner: dict
    votes: int


class UpdatePost(BaseModel):
    title: str
    content: str
    # tags later

class CommentResponse(BaseModel):
    id: int
    content: str
    post_id: int
    owner_id: int
    created_at: datetime

class CommentCreate(BaseModel):
    content: str

class CreateCommentOut(BaseModel):
    id: int
    content: str
    owner: dict

class Vote(BaseModel):
    post_id: int
    dir: int  # 1 for upvote, 0 for remove vote

class UserResponse(BaseModel):
     id: int
     username: str
     email: EmailStr
     posts_count: int
     comments_count: int
     votes_count: int

     class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserCreateOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    created_at:datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class PostCreate(PostBase):
    title: str
    content: str

class Token(BaseModel):
    access_token: str
    token_type: str