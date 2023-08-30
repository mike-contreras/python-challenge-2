from peewee import CharField, ForeignKeyField, DecimalField
from uuid import uuid4
from .account import Account
from .basemodel import BaseModel

class Card(BaseModel):
    
    card_number = CharField(unique=True, default=str(uuid4())[:16])
    cvv = CharField(unique=True, default=str(uuid4())[:3])
    account = ForeignKeyField(Account)
    balance = DecimalField(default=0)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def expense(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Insufficient balance")


    def describe(self):
        print(f'Card account_id: {self.account}, card_number: {self.card_number}, balance: {self.balance}, cvv: {self.cvv}')