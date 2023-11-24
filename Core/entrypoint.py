"""This will be the main entry point for application"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from Identity.database import MongoDBClient
from Core.settings import Settings
from Core.sso_config import SSOConfig
from Core.models import ResponseModel

settings = Settings.get_settings()
class SSOApp:
    def __init__(self):
        self.app = FastAPI(
            title=settings.APP_TITLE,
            description="SSO application using fastapi and mongodb",
            summary="SSO application for projects",
            version="0.0.1",
            contact={
                "name": "M. Irtaza Hussain",
                "url": "https://mihussain.vercel.app/",
                "email": "mihussain.official@gmail.com",
            },
            license_info={
                "name": "Unlincesed",
                "url": "https://github.com/IrtazaHussain1/SSO/blob/main/LICENSE",
            },
        )
        self.config = SSOConfig()
        self.db_client = MongoDBClient()
        self.oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token", authorizationUrl="/auth")

        @self.app.post("/auth")
        def generate_token(username: str, password: str) -> dict:
            response: ResponseModel = self.db_client.validate_user(username=username, password=password)
            if not response.status:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=response.message,
                    headers={"WWW-Authenticate": "Bearer"},
                )

            token_data = {"sub": response.data}
            return {"access_token": self.config.create_jwt_token(token_data), "token_type": "bearer"}

        @self.app.get("/profile", response_model=dict)
        def get_profile(current_user: dict = Depends(self.config.get_current_user)):
            return current_user
        
        @self.app.get("/")
        def read_root():
            return {"Hello": "World tnis is test"}

    
    @classmethod
    def get_app(cls):
        return cls().app
