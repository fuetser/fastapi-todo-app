from fastapi import APIRouter, Depends
from models.todos import TODO, TODOCreate, TODOUpdate
from services.todos import TodosService


router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[TODO])
def get_all_todos(service: TodosService = Depends()):
    return service.get_all()


@router.get("/{todo_id}", response_model=TODO)
def get_todo_by_id(todo_id: int, service: TodosService = Depends()):
    return service.get(todo_id)


@router.post("/", response_model=TODO)
def create_todo(data: TODOCreate, service: TodosService = Depends()):
    return service.create(data)


@router.put("/{todo_id}", response_model=TODO)
def update_todo(todo_id: int, data: TODOUpdate, service: TodosService = Depends()):
    return service.update(todo_id, data)


@router.delete("/{todo_id}", response_model=TODO)
def delete_todo(todo_id: int, service: TodosService = Depends()):
    return service.delete(todo_id)
