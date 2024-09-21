from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from blog.database import Base


class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key = True, unique= True, index = True)
    title = Column(String)
    body= Column(String)