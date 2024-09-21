from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# creating an engine
SQLALCHEMY_DATABASE_URL = 'sqlite+pysqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, 
                       connect_args={"check_same_thread": False},echo = True)


# creating session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




Base = declarative_base()


# create settings for db connection
# when we are done, next how do we use this connection