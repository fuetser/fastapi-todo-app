from fastapi import APIRouter, Depends
from models.todos import TODO
from services.todos import TodosService


router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[TODO])
def get_all_todos(todos_service: TodosService = Depends()):
    return todos_service.get_all()
