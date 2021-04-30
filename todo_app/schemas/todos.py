from typing import Optional
from pydantic import BaseModel, constr


class TodoBaseModel(BaseModel):
    title: constr(max_length=64, min_length=1)
    description: constr(max_length=128) = None
    owner_id: int

    class Config:
        extra = "forbid"


class TodoCreateModel(TodoBaseModel):
    pass


class TodoUpdateModel(BaseModel):
    title: Optional[constr(max_length=64, min_length=1)]
    description: Optional[constr(max_length=128)] = None

    class Config:
        extra = "forbid"


class TodoModel(TodoBaseModel):
    id: int

    class Config:
        orm_mode = True
