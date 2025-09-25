from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/comments",tags=["Comments"]
)


@router.post("/{post_id}",status_code=status.HTTP_201_CREATED,response_model=schemas.CommentResponse)
def create_comment(post_id:int,comment:schemas.CommentCreate,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    new_comment=models.Comment(owner_id=current_user.id,**comment.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/{post_id}",response_model=List[schemas.CommentResponse])
def get_post_comments(post_id:int,db:Session=Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.post_id==post_id).all()
    return comments