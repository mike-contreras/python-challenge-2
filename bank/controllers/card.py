from ..models.account import Account
from ..models.card import Card

class CardController:
    
    @staticmethod
    def create(account: Account, balance: float) -> Card:
        card = Card(account=account.id, balance=balance)
        card.save()
        return card

    @staticmethod
    def get_by_id(card_id:int): 
        try:
            return Card.get(id=card_id)
        except Card.DoesNotExist:
            print('Card not found.')
            return None

    @staticmethod
    def get_by_Account(account: Account):
        try:
            return Card.get(account=account.id)
        except Card.DoesNotExist:
            print('Card not found.')
            return None
    
    @staticmethod
    def delete(card: Card):
        try:
            card.delete_instance()
        except Card.DoesNotExist:
            print('Card not found')