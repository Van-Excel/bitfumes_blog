from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from ..models import Blog

from ..db import get_db

from ..schemas import BlogCreate, BlogResponse, SingleBlog
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..main import models


router = APIRouter(tags=["Blog"])


hash = Hash()


@router.post(
    "/blog",
    response_model=BlogResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_blog(blog: BlogCreate, session: Session = Depends(get_db)):
    new_book = models.Blog(title=blog.title, body=blog.body, user_id=1)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


@router.get(
    "/blogs",
    response_model=List[BlogResponse],
    status_code=status.HTTP_200_OK,
)
async def get_blogs(session: Session = Depends(get_db)):
    # statement = select(models.Blog).order_by(models.Blog.title)
    # result = session.execute(statement)
    # results = result.scalars().all() # Returns a list of tuples containing Blog objects
    blogs = session.query(Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Blogs not found"
        )
    return blogs


@router.get(
    "/blog/{id}",
    response_model=SingleBlog,
    status_code=status.HTTP_200_OK,
)
async def get_single_blog(id: int, session: Session = Depends(get_db)):
    # sqlalachemy doesn't have where function
    blog = session.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID of {id} not found",
        )
    return blog


@router.delete(
    "/blog/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_blog(id: int, session: Session = Depends(get_db)):

    blog = session.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID of {id} not found",
        )

    session.delete(blog)
    session.commit()

    return {"message": "Resource deleted"}


@router.patch("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(
    id: str, blog_update: BlogCreate, session: Session = Depends(get_db)
):
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
    blog = session.query(Blog).filter(Blog.id == id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with ID of {id} not found",
        )

    blog.update(blog_update_dict)
    session.commit()
    return {"message": "Resource updated successfully"}
