import unittest
from peewee import SqliteDatabase
from ..models.account import Account
from ..controllers.account import AccountController

class TestAccountController(unittest.TestCase):
    def setUp(self):
        self.test_db = SqliteDatabase(':memory:')
        User._meta.database = self.test_db
        self.test_db.connect()
        self.test_db.create_tables([User], safe=True)

    def tearDown(self):
        self.test_db.drop_tables([User])
        self.test_db.close()

    def test_initialize_correctly(self):
        user = AccountController.create(name='test_user', email='test@email.com', age=20)
        assert isinstance(user, User), 'User should be created'

if __name__ == '__main__':
    unittest.main()