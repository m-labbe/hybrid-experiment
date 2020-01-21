import pytest

from app import app
from database import session, engine
from todo_item import TodoItem


@pytest.fixture(autouse=True)
def auto_rollback():
    for item in session.query(TodoItem).all():
        session.delete(item)
    session.flush()
    engine.commit = lambda: None
    yield
    session.rollback()
