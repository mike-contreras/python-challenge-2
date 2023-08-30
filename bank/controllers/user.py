from typing import Union
from ..models.account import Account
from ..models.user import User
from .account import AccountController

class UserController:
    
    @staticmethod
    def create( name: str, email: str, age: int) -> User:
        user = User(name=name, age=age, email=email)
        user.save()
        return user
    
    @staticmethod
    def update_name( user: User, name: str) -> User:
        user.name = name
        user.save()
        return user

    @staticmethod
    def get_user_by_id(user_id: int) -> Union[User, None]:
        assert isinstance(user_id, int), 'user_id must be int'

        try:
            return User.get(id=user_id)
        except User.DoesNotExist:
            print('User not found.')
            return None

    @staticmethod
    def get_user_by_name(name: str) -> Union[User, None]:
        # Validations
        assert len(name) > 0, "Name can't be empty"

        try:
            return User.get(name=name)
        except User.DoesNotExist:
            print('User not found.')
            return None

    @staticmethod
    def delete(user: User):
        # Validations
        assert isinstance(user, User), 'user must be instance of User class'

        try:
            account = Account.get(user_id=user.id)
            AccountController.delete(account)
            user.delete_instance()
        except Account.DoesNotExist:
            account = None
            user.delete_instance()