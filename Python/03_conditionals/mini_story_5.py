order_amount = float(input("How much is the order? "))

delivery_fee = 0 if order_amount > 300 else 30 # Ternary operator to determine delivery fee based on order amount
print(f"The delivery fee is ${delivery_fee:.2f}")