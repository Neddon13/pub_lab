import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Lucky Pub", 1000, "wine")

    def test_pub_has_name(self):
        self.assertEqual("Lucky Pub", self.pub.name)