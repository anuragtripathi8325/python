from fastapi import APIRouter

from controllers import register_user
from schemas import UserCreate

router = APIRouter()


@router.post("/register")
def register(data: UserCreate):
    return register_user(data)