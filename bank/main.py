from .models.account import Account
from .models.card import Card
from .models.user import User
from .models.basemodel import db
from .controllers.user import UserController
from .controllers.account import AccountController
from .controllers.card import CardController
from .util import print_tables


def setup_database():
    # db.init('bank.db')
    db.init(':memory:')
    db.connect()
    db.create_tables([User, Account, Card])
def teardown_database():
    db.close()

def main():
    setup_database()
    smith = UserController.create(name='John Smith', age=40, email='john@email.com')
    smith_account = AccountController.create(user=smith, balance=30000)
    smith_card = CardController.create(account=smith_account, balance=20000)

    print('Initial:')
    print_tables()
    
    UserController.update_name(user=smith, name='David Copperfield')
    AccountController.update(account=smith_account, amount=-80000)

    AccountController.update(account=smith_account, amount=55000)

    print('After update:')
    print_tables()
    
    print('smith_card:', smith_card)
    CardController.delete(card=smith_card)
    AccountController.delete(account=smith_account)
    UserController.delete(user=smith)

    # Print deleted results
    print('End:')
    print_tables()
    teardown_database()

if __name__ == "__main__":
    main()