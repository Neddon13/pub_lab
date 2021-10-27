import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Lucky Pub", 1000, "wine")
        self.drink= Drink("wine", 25)

    def test_pub_has_name(self):
        self.assertEqual("Lucky Pub", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_has_drink(self):
        self.assertEqual("wine", self.drink.beverage)