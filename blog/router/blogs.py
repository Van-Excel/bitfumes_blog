from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from ..models import Blog

from ..db import get_db

from ..schemas import BlogCreate, BlogResponse, SingleBlog
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..main import models
from ..services.blog import Blogs


router = APIRouter(tags=["Blog"])


hash = Hash()
blogs = Blogs()


@router.post(
    "/blog",
    response_model=BlogResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_blog(blog: BlogCreate, session: Session = Depends(get_db)):

    return blogs.create(blog, session)


@router.get(
    "/blogs",
    response_model=List[BlogResponse],
    status_code=status.HTTP_200_OK,
)
async def get_blogs(session: Session = Depends(get_db)):
    # statement = select(models.Blog).order_by(models.Blog.title)
    # result = session.execute(statement)
    # results = result.scalars().all() # Returns a list of tuples containing Blog objects
    return blogs.retrieve_all(session)


@router.get(
    "/blog/{id}",
    response_model=SingleBlog,
    status_code=status.HTTP_200_OK,
)
async def get_single_blog(id: int, session: Session = Depends(get_db)):
    # sqlalachemy doesn't have where function
    return blogs.retrieve(id, session)


@router.delete(
    "/blog/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_blog(id: int, session: Session = Depends(get_db)):

    return blogs.delete(id, session)


@router.patch("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_blog(
    id: str, blog_update: BlogCreate, session: Session = Depends(get_db)
):
    return blogs.delete(id, blog_update, session)
