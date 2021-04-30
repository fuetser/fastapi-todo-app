from fastapi import HTTPException
from models import Todo
from schemas import TodoCreateModel, TodoUpdateModel
from .users import UserService


class TodoService():
    @staticmethod
    async def get_all() -> list[Todo]:
        return await Todo.all()

    @staticmethod
    async def get(todo_id: int, get_query: bool = False) -> Todo:
        todo = Todo.filter(id=todo_id)
        if not get_query:
            todo = await todo.first()
        todo_exists_query = await todo.exists() if get_query else True
        if not todo or not todo_exists_query:
            raise HTTPException(
                status_code=404,
                detail=f"Todo with id {todo_id} not found"
            )
        return todo

    @staticmethod
    async def create(todo_data: TodoCreateModel) -> Todo:
        user_exists = await UserService.exists(todo_data.owner_id)
        if not user_exists:
            raise HTTPException(
                status_code=404,
                detail=f"User with id {todo_data.owner_id} not found"
            )
        return await Todo.create(**todo_data.dict())

    @staticmethod
    async def update(todo_id: int, todo_data: TodoUpdateModel) -> Todo:
        todo = await TodoService.get(todo_id, get_query=True)
        await todo.update(**todo_data.dict(exclude_unset=True))
        return await todo.first()

    @staticmethod
    async def delete(todo_id: int) -> Todo:
        todo = await TodoService.get(todo_id)
        todo_query = await TodoService.get(todo_id, get_query=True)
        await todo_query.delete()
        return todo
