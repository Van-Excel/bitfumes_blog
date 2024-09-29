from fastapi import HTTPException, status
from ..schemas import BlogCreate, BlogResponse, SingleBlog

from .. import models
from sqlalchemy.orm import Session


class Blogs:

    def create(self, blog: BlogCreate, session: Session):

        new_book = models.Blog(title=blog.title, body=blog.body, user_id=1)
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        return new_book

    def retrieve_all(self, session: Session):
        blogs = session.query(models.Blog).all()
        if not blogs:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"Blogs not found"
            )

        return blogs

    def retrieve(self, id: int, session: Session):
        blog = session.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID of {id} not found",
            )
        return blog

    def delete(self, id: int, session: Session):
        blog = session.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID of {id} not found",
            )

        session.delete(blog)
        session.commit()

        return {"message": "Resource deleted"}

    def patch(id: str, blog_update: BlogCreate, session: Session):

        # Convert blog_update to a dictionary
        # blog_update_dict = blog_update.dict(exclude_unset=True)  # This excludes fields that were not set
        blog_update_dict = blog_update.model_dump()

        # Build the update statement
        # stmt = (
        # update(Blog)
        # .where(Blog.id == id)
        # .values(blog_update_dict)
        # .execution_options(synchronize_session="fetch")
        # )
        # Execute the statement
        # session.execute(stmt)
        # session.commit
        blog = session.query(models.Blog).filter(models.Blog.id == id)
        if not blog:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with ID of {id} not found",
            )

        blog.update(blog_update_dict)
        session.commit()
        return {"message": "Resource updated successfully"}
