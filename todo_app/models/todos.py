from pydantic import BaseModel


class TODO(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
