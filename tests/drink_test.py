import unittest
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("wine", 7)
