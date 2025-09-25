from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/admin",tags=["Admin"])

@router.delete("/user/{id}",status_code=status.HTTP_204_NO_CONTENT)
def admin_delete_user(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    user_query=db.query(models.User).filter(models.User.id==id)
    user=user_query.first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} does not exist")
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform requested action")
    user_query.delete(synchronize_session=False)
    db.commit()
    return{"message":"user successfully deleted"}

@router.delete("/post/{id}",status_code=status.HTTP_204_NO_CONTENT)
def admin_delete_post(id:int,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} does not exist")
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return{"message":"post successfully deleted"}

@router.get("/users",response_model=List[schemas.UserResponse])
def get_all_users(db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform requested action")
    users = db.query(models.User).all()
    return users