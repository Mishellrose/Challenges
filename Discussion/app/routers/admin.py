from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,oauth2,database
from ..database import get_db
from typing import List

router=APIRouter(
    prefix="/admin",tags=["Admin"])

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(database.get_db), admin=Depends(oauth2.get_current_admin)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
     
    

@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(database.get_db), admin=Depends(oauth2.get_current_admin)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}


@router.get("/users/{user_id}", response_model=List[schemas.UserOut])
def get_all_users(db: Session = Depends(database.get_db), admin=Depends(oauth2.get_current_admin)):
    users = db.query(models.User).all()
    return users