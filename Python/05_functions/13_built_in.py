def chai_flavour(flavour="Masala"):
    '''This function returns the flavour of chai.'''
    return f"Your chai flavour is {flavour}."

print(chai_flavour())
print(chai_flavour("Ginger"))
print(chai_flavour.__doc__)
print(chai_flavour.__name__)

def generate_bill(amount, tax=0.05):
    '''This function generates a bill with tax.
    :param amount: The amount of the bill.
    :param tax: The tax percentage to be applied on the amount. Default is 0.05 (5%).
    :return: A string representing the total bill amount.
    '''
    total = amount + (amount * tax)
    return f"Your total bill is {total:.2f}."

print(generate_bill(100))
print(generate_bill(100, 0.1))
print(generate_bill.__doc__)