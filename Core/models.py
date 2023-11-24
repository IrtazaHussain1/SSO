from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    status: str | bool
    message: Optional[str]
    data:  Optional[str]