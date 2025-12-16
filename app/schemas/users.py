from typing import Annotated

from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    username: Annotated[str, Field(min_length=5, max_length=100)]
    password: Annotated[str, Field(min_length=8, max_length=20)]
    confirm: Annotated[str, Field(min_length=8, max_length=20)]
    

class UserResponse(BaseModel):
    username: Annotated[str, Field(min_length=5, max_length=100)]
    password: Annotated[str, Field(min_length=8, max_length=255)]
    role: str

    class Config:
        from_attributes = True
        