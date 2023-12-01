"""This will be the main entry point for application"""
from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from Core.settings import Settings
from Identity.routes import router as SSO_Router

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
        self.app.include_router(SSO_Router)
        self.oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token", authorizationUrl="/sso/auth")

    @classmethod
    def get_app(cls):
        return cls().app
