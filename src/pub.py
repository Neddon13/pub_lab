class Pub:
    
    def __init__(self, name, till, drink):
        self.name = name
        self.till = till
        self.drink = []

    def add_to_till(self, amount):
        self.till += amount
