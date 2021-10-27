import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Sam", 100)
        self.drinks = Drink("wine", 25)
        self.wallet = Customer("Sam", 100)

    def test_customer_has_name(self):
        self.assertEqual("Sam", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)
    
    def test_can_add_beverage(self):
        self.customer.add_drink(self.drinks)
        self.assertEqual(1, self.customer.drinks)

    def test_can_reduce_wallet(self):
        self.customer.reduce_wallet(25)
        self.assertEqual(75, self.customer.wallet)

    # def test_customer_can_buy_beverage(self):
    #     self.customer.