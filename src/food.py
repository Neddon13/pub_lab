class Food:

    def __init__(self, name, price, bill):
        self.name = name
        self.price = price
        self.bill = bill

    def add_to_tab(self, price):
        self.bill += price
        

