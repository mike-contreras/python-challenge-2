from peewee import  CharField, AutoField, IntegerField
from .basemodel import BaseModel

class User(BaseModel):
    id = AutoField()
    name = CharField()
    email = CharField(unique=True)
    phone = CharField(null=True)
    age = IntegerField(null=False)

    def describe(self):
        print(f'id: {self.id}, name: {self.name}, email: {self.email}, phone: {self.phone}, age: {self.age},')
