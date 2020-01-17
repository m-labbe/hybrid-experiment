from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"text": "I love it when a plan comes together!"}


@app.get("/todo/")
def read_item():
    return {"status": "success"}


@app.post("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}


@app.put("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}


@app.delete("/todo/{todo_id}")
def read_item(todo_id: int):
    return {"todo_id": todo_id}
