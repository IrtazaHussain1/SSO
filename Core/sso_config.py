from fastapi import HTTPException, status
from jose import JWTError, jwt
from Core.constants import jwt_secret_key, jwt_hash_algo

class SSOConfig:
    def __init__(self):
        self.secret_key = jwt_secret_key
        self.algorithm = jwt_hash_algo

    def create_jwt_token(self, data: dict) -> str:
        return jwt.encode(data, self.secret_key, algorithm=self.algorithm)

    def get_current_user(self, token: str) -> dict:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            print(token)
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            raise credentials_exception
