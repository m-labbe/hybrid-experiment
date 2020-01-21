import json
import logging
from starlette.testclient import TestClient
from app import app
from todo_item import TodoItem
from database import session

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

client = TestClient(app)


def test_get_all():
    item1 = TodoItem(completed=False, text="Test item text")
    session.add(item1)
    item2 = TodoItem(completed=False, text="Test item two text")
    session.add(item2)
    item3 = TodoItem(completed=True, text="Test item three text")
    session.add(item3)
    session.flush()
    response = client.get("/todo/")
    actual = response.json()
    expected = {
        "status": "success",
        "data": [
            {"id": item1.id, "completed": False, "text": "Test item text"},
            {"id": item2.id, "completed": False, "text": "Test item two text"},
            {"id": item3.id, "completed": True, "text": "Test item three text"},
        ],
    }
    assert actual == expected


def test_add_item():
    client.post("/todo/", json={"completed": False, "text": "Add new item"})
    actual = session.query(TodoItem).filter(TodoItem.text == "Add new item").one()
    assert actual.text == "Add new item"
    assert actual.completed == False


def test_delete_item():
    delete_me = TodoItem(id=1, completed=False, text="Delete this item")
    session.add(delete_me)
    session.flush()
    client.delete("/todo/1/")
    actual = session.query(TodoItem).filter_by(id=1).first()
    assert actual is None


def test_update_item_completed():
    item = TodoItem(id=1, completed=False, text="Test item three text")
    session.add(item)
    session.flush()
    client.put("/todo/1/", json={"completed": True})
    actual = session.query(TodoItem).filter_by(id=1).one()
    assert actual.completed


def test_update_item_text():
    item = TodoItem(id=1, completed=False, text="Test item three text")
    session.add(item)
    session.flush()
    client.put("/todo/1/", json={"text": "My new text"})
    actual = session.query(TodoItem).filter_by(id=1).one()
    assert actual.text == "My new text"
