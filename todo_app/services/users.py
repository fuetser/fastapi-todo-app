import bcrypt
from fastapi import HTTPException
from models import User
from schemas import UserCreateModel, UserUpdateModel


class UserService():
    @staticmethod
    async def get_all() -> list[User]:
        return await User.filter().prefetch_related("todos").all()

    @staticmethod
    async def get(user_id: int, get_query: bool = False) -> User:
        user = User.filter(id=user_id).prefetch_related("todos")
        user_exists = await user.exists() if not not get_query else True
        if not get_query:
            user = await user.first()
        if not user or not user_exists:
            raise HTTPException(
                status_code=404,
                detail=f"User with id {user_id} not found"
            )
        return user

    @staticmethod
    async def create(user_data: UserCreateModel) -> User:
        await UserService.validate_username(user_data.username)
        user_data.password = UserService.hash_password(user_data.password)
        user = await User.create(**user_data.dict())
        await user.fetch_related("todos")
        return user

    @staticmethod
    async def update(user_id: int, user_data: UserUpdateModel) -> User:
        user_query = await UserService.get(user_id, get_query=True)
        if user_data.username != (await user_query.first()).username:
            await UserService.validate_username(user_data.username)
        if user_data.password:
            user_data.password = UserService.hash_password(user_data.password)
        await user_query.update(**user_data.dict(exclude_unset=True))
        return await user_query.first()

    @staticmethod
    async def delete(user_id) -> User:
        user = await UserService.get(user_id)
        user_query = await UserService.get(user_id, get_query=True)
        await user_query.delete()
        return user

    @staticmethod
    async def validate_username(username) -> None:
        user_exists = await User.get(username=username).exists()
        if user_exists:
            raise HTTPException(
                status_code=409,
                detail=f"Username {username} is already taken"
            )

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(rounds=10)
        ).decode("utf-8")

    @staticmethod
    async def exists(user_id: int) -> bool:
        user_query = await UserService.get(user_id, get_query=True)
        return await user_query.exists()
