from fastapi import HTTPException, status
from fastapi.templating import Jinja2Templates
from Core.models import ResponseModel
from Core.models import ResponseModel
from Core.sso_config import SSOConfig
from Identity.database import MongoClient

templates = Jinja2Templates(directory="templates")


def authenticate(username, password):
    db_client = MongoClient()
    config = SSOConfig()
    response: ResponseModel = db_client.validate_user(username=username, password=password)
    if not response.status:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=response.message,
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {"sub": response.data}
    return {"access_token": config.create_jwt_token(token_data), "token_type": "bearer"}


def index(request):
    return templates.TemplateResponse("auth.html", context={'request': request})

def logout():
    ...

def profile():
    ...
