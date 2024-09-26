from typing import List
from blog.models import Blog, User
from fastapi import FastAPI, Depends, status, HTTPException
import uvicorn
from blog.schemas import BlogCreate, BlogResponse, SingleBlog, User, UserResponse
from . import models
from blog.hashing import Hash
from blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import update


tags_metadata = [
    {
        "name": "Blog",
        "description": "Operations for Blogs.",
    },
    
    {
        "name": "Users",
        "description": "APIs for User Management and Authentication.",
    },
]

app = FastAPI(
    title="buildlyAPI",
    description="APIs for Blogs and User Management",

    version="0.0.1",
    openapi_tags= tags_metadata,
)

# create database tables (DDL)
models.Base.metadata.create_all(engine)

# create session


hash = Hash()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/blog",
    response_model=BlogResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Blog"],
)
async def create_blog(blog: BlogCreate, session: Session = Depends(get_db)):
    new_book = models.Blog(title=blog.title, body=blog.body, user_id = 1)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)

    return new_book


@app.get(
    "/blogs",
    response_model=List[BlogResponse],
    status_code=status.HTTP_200_OK,
    tags=["Blog"],
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


@app.get(
    "/blog/{id}",
    response_model=SingleBlog,
    status_code=status.HTTP_200_OK,
    tags=["Blog"],
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


@app.delete(
    "/blog/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Blog"],
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


@app.patch("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
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


######################################################################


@app.post(
    "/user",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
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

@app.delete(
    "/user/{id}",
    
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
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

    


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app", port=8000, log_level="info", reload=True, use_colors=True
    )
    server = uvicorn.Server(config)
    server.run()
