from fastapi import FastAPI
import uvicorn

from . import models
from .database import engine
from .router import users, blogs


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
    openapi_tags=tags_metadata,
)

app.include_router(users.router)
app.include_router(blogs.router)

# create database tables (DDL)
models.Base.metadata.create_all(engine)

######################################################################


if __name__ == "__main__":
    config = uvicorn.Config(
        "blog.main:app", port=8000, log_level="info", reload=True, use_colors=True
    )
    server = uvicorn.Server(config)
    server.run()
