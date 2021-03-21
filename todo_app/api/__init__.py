from fastapi import APIRouter
from api import todos


router = APIRouter()
router.include_router(todos.router)
