from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List,Optional
from pydantic.types import conint

class User(BaseModel):
    username:str
    email:EmailStr

class UserCreate(User):
    password: str

class UserOut(User):
    id:int
    created_at:datetime
    posts_count:int
    votes:int
    comments_count:int
    class Config:
        from_attributes:True

class Post(BaseModel):
    title:str
    content:str

    
class PostCreateOut(Post): 
    id:int
    owner_id:int
    created_at:datetime
    class config:
        from_attributes:True


class AllPostsOut(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    created_at: datetime
    votes: int
    owner: UserOut

    class Config:
        orm_mode = True 
    
    

class UpdateOut(Post):
    id:int
    owner_id:int
    created_at:datetime
    class config:
        from_attributes=True

class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)

class Comment(BaseModel):
    content:str

class CommentOut(Comment):
    id:int
    owner_post:PostCreateOut
    owner:User
    class Config:
        from_attributes=True

class CommentGet(BaseModel):
    id:int
    content:str
    owner:UserOut
    class Config:
        orm_mode=True
        
class AdminLogin(BaseModel):
    email:EmailStr
    password:str
    
class AdminOut(User):
    id:int
    posts_count:int     
    comments_count:int  
    votes_count:int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]=None
    type:Optional[str]=None
