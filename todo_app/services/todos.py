from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_session
from tables import TODO


class TodosService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[TODO]:
        todos = self.session.query(TODO).all()
        return todos
