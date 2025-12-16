from typing import Annotated

from pydantic import BaseModel, Field


class UserLogin(BaseModel):
    username: Annotated[str, Field(min_length=5, max_length=100)]
    password: Annotated[str, Field(min_length=8, max_length=20)]


class TokenResponse(BaseModel):
    token: Annotated[str, Field(min_length=5, max_length=100)]
