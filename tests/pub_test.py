import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer_1 = Customer("Ben", 10, 18, 0)
        self.customer_2 = Customer("Adam", 1, 12, 0)
        self.drink_1 = Drink("Tennents", 2, 1)
        self.drink_2 = Drink("wine", 4, 2)
        self.drink_3 = Drink("gin", 5, 3)



    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.pub_name)

    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_money(self):
        self.assertEqual(100, self.pub.till)
        
    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(0, self.pub.stock_count())

    def test_pub_can_add_drinks(self):
        self.pub.add_drink(self.drink_1)
        self.assertEqual(1, self.pub.stock_count()) 

    #@unittest.skip("Delete this line to run the test")
    def test_customer_has_money(self):
        self.assertEqual(True, self.pub.check_customer_wallet(self.customer_1, self.drink_1))

    #@unittest.skip("Delete this line to run the test"
    def test_customer_has_money(self):
        self.assertEqual(False, self.pub.check_customer_wallet(self.customer_2, self.drink_1))

    def test_customer_money_reduced(self):
        self.assertEqual(8, self.pub.take_customer_money(self.customer_1, self.drink_1))
    
    def test_add_money_to_till(self):
        self.assertEqual(102, self.pub.add_to_till(self.customer_1, self.drink_1))

    def test_customer_id(self):
        self.assertEqual(True, self.pub.age_id(self.customer_1))

    def test_customer_id(self):
        self.assertEqual(False, self.pub.age_id(self.customer_2))

    def test_customer_drunk(self):
        self.assertEqual(1, self.pub.get_customer_drunk(self.customer_1, self.drink_1))

    def test_pub_can_serve_drink(self):
        self.pub.add_drink(self.drink_1)
        self.pub.add_drink(self.drink_2)
        self.pub.serve(self.customer_1, self.drink_1)
        self.assertEqual(8.00, self.customer.wallet)
        self.assertEqual(102.00, self.pub.till)
        self.assertEqual(1, self.pub.drink_count())
    




