from fastapi import APIRouter
from Identity.controller import authenticate


router = APIRouter(prefix="/sso")


@router.post("/auth")
def generate_token(username: str, password: str) -> dict:
    return authenticate(username, password)

# @router.get("/profile", response_model=dict)
# def get_profile(current_user: dict = Depends(self.config.get_current_user)):
#     return current_user

@router.get("/")
def read_root():
    return {"Hello": "World tnis is test"}