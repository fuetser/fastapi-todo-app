from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_session
from models.todos import TODOCreate, TODOUpdate
from tables import TODO


class TodosService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[TODO]:
        todos = self.session.query(TODO).all()
        return todos

    def get(self, todo_id: int) -> TODO:
        todo = self.session.query(TODO).get(todo_id)
        if not todo:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return todo

    def create(self, todo_data: TODOCreate) -> TODO:
        todo = TODO(**todo_data.dict())
        self.session.add(todo)
        self.session.commit()
        return todo

    def update(self, todo_id: int, todo_data: TODOUpdate) -> TODO:
        todo = self.get(todo_id)
        for key, value in todo_data:
            setattr(todo, key, value)
        self.session.commit()
        return todo

    def delete(self, todo_id: int) -> None:
        todo = self.get(todo_id)
        self.session.delete(todo)
        self.session.commit()
