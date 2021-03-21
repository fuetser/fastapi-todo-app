from pydantic import BaseModel


class TODOBase(BaseModel):
    title: str
    description: str
    owner_id: int


class TODOCreate(TODOBase):
    pass


class TODOUpdate(TODOBase):
    pass


class TODO(TODOBase):
    id: int

    class Config:
        orm_mode = True
