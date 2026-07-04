from fastapi import Depends, FastAPI, HTTPException 
from sqlalchemy.orm import Session
from database.db import Base, Task, addTask, engine, get_db



app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager"}


@app.get("/alltask")
def all_task(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.post("/createtask")
def create_task(task_data: addTask, db: Session = Depends(get_db)):
    db_item = Task(**task_data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/task/{id}")
def read_task(id:int, db: Session=Depends(get_db)):
    db_item = db.query(Task).filter(Task.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

