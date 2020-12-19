from fastapi import APIRouter, Depends
from pydantic import BaseModel

from services.auth import get_current_user
from models.user import User, User_Pydantic, UserIn_Pydantic


tags = ["users"]
router = APIRouter()


class UserIn(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register", tags=tags, response_model=User_Pydantic)
async def register_user(form_data: UserIn):
    return await User.create(**form_data.dict(exclude_unset=True))


@router.get("/current_user", tags=tags, response_model=User_Pydantic)
async def get_user_data(user: User = Depends(get_current_user)):
    return user


@router.patch("/current_user", tags=tags, response_model=User_Pydantic)
async def update_user(form_data: UserIn_Pydantic, user: User = Depends(get_current_user)):
    await user.update_from_dict(form_data.dict(exclude_unset=True)).save()
    return user
