import unittest 
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Ben", 10)

    def test_customer_has_name(self):
        self.assertEqual("Ben", self.customer.customer_name)

    def test_customer_has_money(self):
        self.assertEqual(10, self.customer.wallet)