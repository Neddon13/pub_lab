import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Sam", 100)
        self.drink = Drink("wine", 25, 7)

    def test_customer_has_name(self):
        self.assertEqual("Sam", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)
    
    def test_can_add_drunkeness(self):
        self.customer.add_drunkeness(self.drink.alcohol_level)
        self.assertEqual(7, self.customer.drunkeness)

    def test_can_reduce_wallet(self):
        self.customer.reduce_wallet(25)
        self.assertEqual(75, self.customer.wallet)
