from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from blog.database import Base


class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key = True, unique= True, index = True)
    title = Column(String)
    body= Column(String)
    
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, unique= True, index = True)
    name = Column(String(50), unique= True, index = True, nullable=False)
    email = Column(String(50), unique= True, index = True, nullable=False)
    hashedpassword = Column(String(255), nullable=False)