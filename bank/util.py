from .models.user import User
from .models.account import Account
from .models.card import Card

def print_users():
    print('Users:')
    users = User.select()
    if users:
        for user in users:
            user.describe()
    else:
        print('No users')


def print_accounts():
    print('Accounts:')
    accounts = Account.select()
    if accounts:
        for account in accounts:
            account.describe()
    else:
        print('No accounts')


def print_cards():
    print('Cards:')
    cards = Card.select()
    if cards:
        for card in cards:
            card.describe()
    else:
        print('No cards')


def print_tables():
    print_users()
    print_cards()
    print_accounts()
    print('\n')