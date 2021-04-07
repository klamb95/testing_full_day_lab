
class Pub:
    def __init__(self, pub_name, till):
        self.pub_name = pub_name 
        self.till = till
        self.drinks_list = []

    def stock_count(self):
        return len(self.drinks_list)

    def check_customer_wallet(self, customer, drink):
        return customer.wallet >= drink.price

    def take_customer_money(self, customer, drink):
       if self.check_customer_wallet(customer, drink) == True:
        customer.wallet -= drink.price
        return customer.wallet

    def add_to_till(self, customer, drink):
        if self.check_customer_wallet(customer, drink) == True:
            self.till += drink.price
            return self.till

    def age_id(self, customer):
        return customer.age >= 18

    def get_customer_drunk(self, customer, drink):
        if self.check_customer_wallet(customer, drink) == True:
            drink.alcohol_level += customer.drunkenness_level
            return customer.drunkenness_level



    # def sell_drink_to_customer(self, customer, drink):
    #    drink = self.(drink_name)
    #    customer.reduce_cash(pet.price)
    #    self.increase_total_cash(pet.price)
    #    self.increase_pets_sold()
    #    self.remove_pet(pet)
    #    customer.add_pet(pet)