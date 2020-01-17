# from fastapi import FastAPI

# # from starlette.templating import Jinja2Templates

# app = FastAPI()
# # templates = Jinja2Templates(directory="templates")


# @app.get("/")
# def read_root():
#     print("Home directory")
#     return {"text": "I love it when a plan comes together!"}
#     # return templates.TemplateResponse(
#     #     "index.html", {"text": "I love it when a plan comes together!"}
#     # )


# # @app.get("/todo/{todo_id}")
# # def read_item(todo_id: int, q: str = None):
# #     return {"todo_id": todo_id, "q": q}


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
