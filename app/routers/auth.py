from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.users import UserRegister, UserResponse
from app.dependencies import get_db
from app.models.user import User
from app.core.security import hash_password

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

