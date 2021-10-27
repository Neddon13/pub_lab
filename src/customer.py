from src.drink import Drink

class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = 100
        self.drunkeness = 0
        self.age = 21
    
    def add_drunkeness(self, alcohol_level):
        self.drunkeness += alcohol_level 

    def reduce_wallet(self, amount):
        self.wallet -= amount

    # def buy_drink(self, beverage):
