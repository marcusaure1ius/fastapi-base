from typing import (List, Dict)

from fastapi import (APIRouter, Depends, Response, status)

from ..models import user_models
from ..services.user_service import UserService

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/getUsers', response_model=List[user_models.User])
def get_users(offset: int = 0, limit: int = 100, user_service: UserService = Depends()):
    return user_service.get_user_list(offset, limit)

@router.get('/getUserById/{id}', response_model=user_models.User)
def get_user_by_id(id: int, user_service: UserService = Depends()):
    return user_service.get_user_by_id(id)

@router.post('/addUser', response_model=user_models.User, status_code=status.HTTP_201_CREATED)
def create_user(user_data: user_models.UserCreate, user_service: UserService = Depends()):
    return user_service.create_user(user_data)