from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/comments",tags=["Comments"]
)


# @router.post("/{post_id}",status_code=status.HTTP_201_CREATED,response_model=schemas.CommentOut)
# def create_comment(post_id:int,comment:schemas.Comment,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
@router.post("/{post_id}",status_code=status.HTTP_201_CREATED,response_model=schemas.CommentOut)
def create_comment(post_id:int,comment:schemas.Comment,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    new_comment=models.Comment(**comment.dict(),postc_id=post_id,userc_id=current_user.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/{post_id}",response_model=List[schemas.CommentOut])
def get_post_comments(post_id:int,db:Session=Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.postc_id==post_id).all()
    if not comments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"comment with  post id: {post_id} does not exist")
    #  posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        # models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    return comments