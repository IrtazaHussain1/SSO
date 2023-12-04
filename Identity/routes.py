from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from Identity.controller import authenticate, index


router = APIRouter(prefix="/sso")
templates = Jinja2Templates(directory="templates")


@router.post("/auth")
def generate_token(username: str, password: str) -> dict:
    return authenticate(username, password)

# @router.get("/profile", response_model=dict)
# def get_profile(current_user: dict = Depends(self.config.get_current_user)):
#     return current_user


@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("auth.html", {'request': request})