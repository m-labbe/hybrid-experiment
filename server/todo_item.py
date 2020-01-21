from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    text = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
