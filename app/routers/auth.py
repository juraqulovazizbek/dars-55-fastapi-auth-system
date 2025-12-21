from typing import Annotated
from datetime import datetime, timedelta

from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.users import UserRegister, UserResponse
from app.schemas.auth import UserLogin, TokenResponse
from app.dependencies import get_db
from app.models.user import User
from app.models.authtoken import AuthToken
from app.core.security import hash_password, verify_password, generate_token

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register', response_model=UserResponse)
def register(
    user_data: UserRegister,
    db: Annotated[Session, Depends(get_db)]
):
    if user_data.password != user_data.confirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Confirm is not the same with password.')
    
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username already exists.')
    
    new_user = User(
        username=user_data.username,
        password=hash_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post('/login', response_model=TokenResponse)
def login(
    credentials: UserLogin,
    db: Annotated[Session, Depends(get_db)]
):
    user = db.query(User).filter(User.username == credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials (username).')
    
    if not verify_password(credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials (password).')
    
    token = AuthToken(
        token=generate_token(),
        expires_date=datetime.now() + timedelta(days=7),
        user_id=user.user_id)
    db.add(token)
    db.commit()
    db.refresh(token)

    return token
