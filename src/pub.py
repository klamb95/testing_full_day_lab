class Pub:
    def __init__(self, pub_name, till):
        self.pub_name = pub_name 
        self.till = till
        self.drinks_list = []

    def stock_count(self):
        return len(self.drinks_list)
