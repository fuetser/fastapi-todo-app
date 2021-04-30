from fastapi import APIRouter
from schemas import TodoModel, TodoCreateModel, TodoUpdateModel
from services import TodoService


router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[TodoModel])
async def get_all_todos():
    return await TodoService.get_all()


@router.get("/{todo_id}", response_model=TodoModel)
async def get_todo_by_id(todo_id: int):
    return await TodoService.get(todo_id)


@router.post("/", response_model=TodoModel)
async def create_todo(data: TodoCreateModel):
    return await TodoService.create(data)


@router.put("/{todo_id}", response_model=TodoModel)
async def update_todo(todo_id: int, data: TodoUpdateModel):
    return await TodoService.update(todo_id, data)


@router.delete("/{todo_id}", response_model=TodoModel)
async def delete_todo(todo_id: int):
    return await TodoService.delete(todo_id)
