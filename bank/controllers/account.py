from ..models.account import Account
from ..models.user import User
from ..models.card import Card

class AccountController:
    
    @staticmethod
    def create(user: User, balance: float) -> Account:
        account = Account(user_id=user.id, balance=balance)
        account.save()
        return account

    @staticmethod
    def get_by_id(account_id:int): 
        assert isinstance(account_id, int), "account_id must be int"
        try:
            return Account.get(id=account_id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    @staticmethod
    def get_by_user(user: User):
        assert isinstance(user, User), "user must be User instance"
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    @staticmethod
    def get_by_card(card: Card):
        assert isinstance(card, Card), "card must be Card instance"
        try:
            return Account.get(id=card.account_id)
        except Account.DoesNotExist:
            print('Account not found.')
            return None

    @staticmethod
    def update(account: Account, amount: float):
        assert isinstance(account, Account ), "account must be Account instance"
        balance = account.balance + amount
        if balance >= 0:
            account.balance = balance
            account.save()
            return True
        else:
            print(f'Invalid balance: {balance}')
            return False
    
    @staticmethod
    def delete(account: Account):
        try:
            card = Card.get(account=account.id)
            card.delete_instance()
            account.delete_instance()
        except Card.DoesNotExist:
            card = None
            account.delete_instance()
