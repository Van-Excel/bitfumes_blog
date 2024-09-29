from fastapi import APIRouter, Depends, HTTPException, status
from ..schemas import User
from sqlalchemy.orm import Session
from ..db import get_db
from ..hashing import Hash
from .. import models


router = APIRouter(tags=["Authentication"])

hash = Hash()


@router.post("/login")
async def login(user: User, session: Session = Depends(get_db)):
    auth_user = (
        session.query(models.User).filter(models.User.email == user.email).first()
    )
    if not auth_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with {user.email} has not signed up",
        )

    if not hash.verifyPassword(user.password, auth_user.hashedpassword):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Password is incorrect"
        )
    # generate token and send to user
    
    return {"user":auth_user.name, "message": "User logged in successfully"}
