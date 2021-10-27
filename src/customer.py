class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drinks = 0
    
    def add_drink(self, drink):
        self.drinks += 1
        return self.drinks

    # def buy_drink(self, beverage):
