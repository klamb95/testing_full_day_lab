class Pub:
    def __init__ (self, name, till):
        self.name = name 
        self.till = till
        self.drinks_list = []

    def stock_count(self):
        return len(self.drinks_list)
