from typing import Annotated

from fastapi.routing import APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.authtoken import AuthToken
from app.schemas.users import UserResponse

router = APIRouter(prefix='/users', tags=['Users'])

token_schema = HTTPBearer()

@router.get('/profile', response_model=UserResponse)
def get(
    token: Annotated[HTTPAuthorizationCredentials, Depends(token_schema)],
    db: Annotated[Session, Depends(get_db)]
):
    existing_token = db.query(AuthToken).filter(AuthToken.token == token.credentials).first()
    if not existing_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token.')
    
    user = existing_token.user

    # if user.role != 'admin':
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not User.')

    return user
