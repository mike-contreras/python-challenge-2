from peewee import  ForeignKeyField, DecimalField, AutoField
from .basemodel import BaseModel
from .user import User

class Account(BaseModel):
        
    id = AutoField()
    balance = DecimalField(default=0)
    user_id = ForeignKeyField(User, backref='accounts')

    def describe(self):
        print(f'Account id= {self.id} userId: {self.user_id}, Balance: {self.balance}')

    