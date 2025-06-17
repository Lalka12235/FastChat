from app.dao.base import BaseDao
from app.users.models import User


class UsersDAO(BaseDao):
    model = User