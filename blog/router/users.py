from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from ..services.users import User

users = User()

from ..db import get_db
from ..schemas import User, UserResponse

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

    return users.create(user, session)


@router.delete(
    "/user/{id}",
    status_code=status.HTTP_201_CREATED,
)
async def delete_user(id: int, session: Session = Depends(get_db)):
    # new_user = user.model_dump()
    return users.delete(id, session)
