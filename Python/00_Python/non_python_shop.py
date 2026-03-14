class Chai:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sip(self):
        return f"You sip the {self.name} and enjoy its flavor."
    
    def add_sugar(self, amount):
        return f"You add {amount} teaspoons of sugar to your {self.name}."
    
    def bill(self):
        return f"The total price for your {self.name} is ${self.price:.2f}."
    
my_chai = Chai("Masala Chai", 3.50)
print(my_chai.add_sugar(2))
print(my_chai.sip())
print(my_chai.bill())