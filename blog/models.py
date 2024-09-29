from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from blog.database import Base


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashedpassword = Column(String(255), nullable=False)

    blogs = relationship("Blog", back_populates="creator")
