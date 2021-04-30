from fastapi import APIRouter
from schemas import UserModel, UserCreateModel, UserUpdateModel
from services import UserService


router = APIRouter(prefix="/users")


@router.get("/", response_model=list[UserModel])
async def get_all_users():
    return await UserService.get_all()


@router.get("/{user_id}", response_model=UserModel)
async def get_user_by_id(user_id: int):
    user = await UserService.get(user_id)
    return user


@router.post("/", response_model=UserModel)
async def create_user(data: UserCreateModel):
    return await UserService.create(data)


@router.put("/{user_id}", response_model=UserModel)
async def update_user(user_id: int, data: UserUpdateModel):
    return await UserService.update(user_id, data)


@router.delete("/{user_id}", response_model=UserModel)
async def delete_user(user_id: int):
    return await UserService.delete(user_id)
