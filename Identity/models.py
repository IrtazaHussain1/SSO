from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    # first_name: Optional[str]
    # last_name: Optional[str]
    username: str
    password: str
    email: str

    def __str__(self) -> str:
        return super().__str__()