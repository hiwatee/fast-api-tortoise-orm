from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.user import User
from services.auth import login_with_password, get_current_user
from services.exceptions import HTTP_404_NOT_FOUND

tags = ["token"]
router = APIRouter()


class GetTokenIn(BaseModel):
    email: str
    password: str


class GetTokenOut(BaseModel):
    token_type: str = "bearer"
    access_token: str
    refresh_token: str


class TokenRefreshIn(BaseModel):
    refresh_token: str


@router.post("/token", tags=tags, response_model=GetTokenOut)
async def get_token_with_password(form_data: GetTokenIn):
    print(form_data)
    user = await login_with_password(form_data.email, form_data.password)
    return GetTokenOut(access_token=user.get_access_token(), refresh_token=user.refresh_token.hex)


@router.post("/refresh_token", tags=tags, response_model=GetTokenOut)
async def token_refresh(form_data: TokenRefreshIn, user: User = Depends(get_current_user)):
    if form_data.refresh_token != user.refresh_token.hex:
        raise HTTP_404_NOT_FOUND
    return GetTokenOut(access_token=user.get_access_token(), refresh_token=user.refresh_token.hex)
