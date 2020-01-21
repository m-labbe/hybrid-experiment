from fastapi import FastAPI
from database import session
from todo_item import TodoItem
from pydantic import BaseModel
from typing import List

app = FastAPI()


class ItemModel(BaseModel):
    id: int
    text: str
    completed: bool

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
    # return {"status": "success", "data": []}


@app.post("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}


@app.put("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}


@app.delete("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}
