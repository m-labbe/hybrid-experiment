from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from database import session
from todo_item import TodoItem
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemModel(BaseModel):
    id: Optional[int]
    text: Optional[str]
    completed: Optional[bool]

    class Config:
        orm_mode = True


class ReadItemResponse(BaseModel):
    status = "success"
    data: List[ItemModel]


@app.get("/")
def read_root():
    return {"text": "I love it when a plan comes together!"}


@app.get("/todo/", response_model=ReadItemResponse)
def read_item():
    items = session.query(TodoItem).order_by(TodoItem.id).all()
    return {"data": items}


@app.post("/todo/")
def create_item(item: ItemModel):
    todo_item = TodoItem(**item.dict())
    session.add(todo_item)
    session.flush()
    session.commit()
    return {"status": "success"}


@app.put("/todo/{todo_id}/")
def update_item(todo_id: int, item: ItemModel):
    todo_item = session.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="Item not found")
    if item.text:
        todo_item.text = item.text
    if item.completed is not None:
        todo_item.completed = item.completed
    session.add(todo_item)
    session.flush()
    session.commit()
    return {"status": "success"}


@app.delete("/todo/{todo_id}/")
def delete_item(todo_id: int):
    todo_item = session.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo_item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(todo_item)
    session.flush()
    session.commit()
    return {"status": "success"}
