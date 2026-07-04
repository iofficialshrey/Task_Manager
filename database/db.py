from sqlalchemy import create_engine, Column, Integer, String
from pydantic import BaseModel
import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base, Session

db_url = "sqlite:///./database.db"
engine = create_engine(db_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autoflush=False, autocommit =False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)

class addTask(BaseModel):
    task: str 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




