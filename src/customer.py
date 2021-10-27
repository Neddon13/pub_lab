from src.drink import Drink

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = 100
        self.drinks = 0
        self.age = 21
    
    def add_drink(self, drink):
        self.drinks += 1
        return self.drinks

    def reduce_wallet(self, amount):
        self.wallet -= amount

    # def buy_drink(self, beverage):
