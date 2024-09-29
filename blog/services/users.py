from fastapi import HTTPException, status
from ..schemas import User

from .. import models
from ..hashing import Hash
from sqlalchemy.orm import Session

hash = Hash()


class User:

    def create(self, user: User, session: Session):
        new_user = models.User(
            name=user.name,
            email=user.email,
            hashedpassword=hash.encryptPassword(user.password),
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def delete(self, id: int, session: Session):

        user = session.query(models.User).filter(models.User.id == id).first()

        if not user:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with ID of {id} not found",
            )
        session.delete(user)
        session.commit()
        return {"message": "User deleted"}
