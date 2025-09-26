

from fastapi import APIRouter, Depends, HTTPException, utils
from sqlalchemy.orm import Session
from app import models, schemas,oauth2
from app.database import get_db


router=APIRouter(tags=["AdminLogin"])

@router.post("/Adminlogin",status_code=200)
def admin_login(creds:schemas.AdminLogin,db:Session=Depends(get_db)):
    admin=db.query(models.Admin).filter(models.Admin.email==creds.email,models.Admin.password==creds.password).first()
    if not admin:
        raise HTTPException(status_code=403,detail="Invalid Credentials")
    
    create_access_token = oauth2.create_access_token(data={"admin_id": admin.id})
    return {"access_token": create_access_token, "token_type": "bearer","message":"Login Successful"}
    
    
    
    
    
    


