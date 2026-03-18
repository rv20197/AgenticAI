customers = ["John", "Jane", "Doe"]
orderBill = ["$10", "$20", "$30"]

for customer, bill in zip(customers, orderBill):
    print(f"Bill for {customer} is {bill}.")