import unittest 
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Ben", 10, 18, 0)


    def test_customer_has_name(self):
        self.assertEqual("Ben", self.customer_1.customer_name)

    def test_customer_has_money(self):
        self.assertEqual(10, self.customer_1.wallet)

    def test_customer_age(self):
        self.assertEqual(18, self.customer_1.age)

    def test_customer_drunkenness_level(self):
        self.assertEqual(0, self.customer_1.drunkenness_level)

    def test_customer_can_buy_drink(self):
        drink = Drink("wine", 4, 1)
        self.customer_1.buy_drink(drink)
        self.assertEqual(6.00, self.customer_1.wallet)

    