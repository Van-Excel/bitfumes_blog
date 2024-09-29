from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class BlogCreate(BaseModel):

    title: str
    body: str

    class Config:
        orm_mode = True


class BlogResponse(BlogCreate):

    pass

    class Config:
        orm_mode = True


class SingleBlog(BlogResponse):
    creator: UserResponse

    class Config:
        orm_mode = True
