from pydantic import BaseModel, EmailStr,conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    username:str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attribute = True

class AllUserOut(BaseModel):
    owner:UserOut
    count:int

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):  
    Post: Post
    votes: int

    class Config:
        from_attribute = True

class UserCreate(BaseModel):
    username:str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
    type:str

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # direction can only be 0 or 1s

class Admin(BaseModel):
    email:EmailStr
    password:str

class Comment(BaseModel):
    content:str

class CommentOut(BaseModel):
    id:int
    content:str
    class Config:
        orm_mode=True