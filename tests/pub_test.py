import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_money(self):
        self.assertEqual(100, self.pub.till)
        
    #@unittest.skip("Delete this line to run the test")
    def test_pub_has_drinks(self):
        self.assertEqual(0, self.pub.stock_count())



