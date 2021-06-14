from typing import (List, Optional)

from fastapi import (Depends, HTTPException, status)
from sqlalchemy.orm import Session

from ..models import user_models
from ..database import tables
from ..database.db_config import get_session


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_user_list(self, offset=0, limit=0) -> List[tables.User]:
        users = (self.session
                 .query(tables.User)
                 .order_by(tables.User.username.desc())
                 .offset(offset)
                 .limit(limit)
                 .all())

        return users

    def get_user_by_id(self, id: int) -> Optional[tables.User]:
        user = (self.session
                .query(tables.User)
                .filter(tables.User.id == id)
                .first())
        return user

    def create_user(self, user_data: user_models.UserCreate) -> tables.User:
        user = tables.User(username=user_data.username, email=user_data.email, password_hash=user_data.password)
        self.session.add(user)
        self.session.commit()
        return user