import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents")

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.name)