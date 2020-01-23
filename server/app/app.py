from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from features.todos import routes as todos


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router)


@app.get("/")
def read_root():
    return {"text": "I love it when a plan comes together!"}
