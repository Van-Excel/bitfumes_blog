from pydantic import BaseModel


class BlogCreate(BaseModel):
    
    title: str
    body:str
    class Config:
        orm_mode = True
        
class BlogResponse(BlogCreate):
    
    pass
    
    class Config:
        orm_mode = True