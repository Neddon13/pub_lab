import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Lucky Pub", 1000, "wine")
        self.drink = Drink("wine", 25, 7)

    def test_pub_has_name(self):
        self.assertEqual("Lucky Pub", self.pub.name)

    def test_pub_has_cash(self):
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_has_drink(self):
        self.assertEqual("wine", self.drink.beverage)

    def test_pub_till_can_increase(self):
        self.pub.add_to_till(25)
        self.assertEqual(1025, self.pub.till)

    def test_pub_can_check_age(self):
        self.assertEqual(True, self.pub.check_age(18))