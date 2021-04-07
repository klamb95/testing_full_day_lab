import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer_1 = Customer("Ben", 10)
        self.customer_2 = Customer("Adam", 1)
        self.drink = Drink("Tennents", 2)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.pub_name)

    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_money(self):
        self.assertEqual(100, self.pub.till)
        
    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(0, self.pub.stock_count())

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_money(self):
        self.assertEqual(True, self.pub.check_customer_wallet(self.customer_1, self.drink))

    #@unittest.skip("Delete this line to run the test"
    def test_customer_has_money(self):
        self.assertEqual(False, self.pub.check_customer_wallet(self.customer_2, self.drink))

    def test_customer_money_reduced(self):
        self.assertEqual(8, self.pub.take_customer_money(self.customer_1, self.drink))
    
    def test_add_money_to_till(self):
        self.assertEqual(102, self.pub.add_to_till(self.customer_1, self.drink))




