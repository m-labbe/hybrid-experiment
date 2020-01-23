import pytest

from database import session, engine
from models.todo_item import TodoItem


@pytest.fixture(autouse=True)
def auto_rollback():
    for item in session.query(TodoItem).all():
        session.delete(item)
    session.flush()
    engine.commit = lambda: None
    yield
    session.rollback()
