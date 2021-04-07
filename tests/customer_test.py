import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Ben", 10, 18)


    def test_customer_has_name(self):
        self.assertEqual("Ben", self.customer_1.customer_name)

    def test_customer_has_money(self):
        self.assertEqual(10, self.customer_1.wallet)

    def test_customer_age(self):
        self.assertEqual(18, self.customer_1.age)

    