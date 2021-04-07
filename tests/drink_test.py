import unittest 
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tennents", 2)

    def test_drink_has_name(self):
        self.assertEqual("Tennents", self.drink.drink_name)

    def test_drink_has_price(self):
        self.assertEqual(2, self.drink.price)