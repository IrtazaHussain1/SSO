from Core.models import ResponseModel
from fastapi import FastAPI, Depends, HTTPException, status
from Core.models import ResponseModel
from Core.sso_config import SSOConfig
from Identity.database import MongoClient



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