import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Steak", 16)


    def test_food_has_price(self):
        self.assertEqual(16, self.food.price)