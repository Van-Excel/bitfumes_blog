from fastapi import APIRouter, Depends, HTTPException, status

from ..main import models


from ..db import get_db
from ..schemas import User, UserResponse
from sqlalchemy.orm import Session
from ..hashing import Hash

hash = Hash()

router = APIRouter(
    tags=["Users"],
)


@router.post(
    "/user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def post_user(user: User, session: Session = Depends(get_db)):
    # new_user = user.model_dump()

    # hashed password

    new_user = models.User(
        name=user.name,
        email=user.email,
        hashedpassword=hash.encryptPassword(user.password),
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.delete(
    "/user/{id}",
    status_code=status.HTTP_201_CREATED,
)
async def delete_user(id: int, session: Session = Depends(get_db)):
    # new_user = user.model_dump()

    user = session.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID of {id} not found",
        )
    session.delete(user)
    session.commit()

    return {"message": "User deleted"}
