tea_flavours = {
    "Green Tea": "out of stock",
    "Black Tea": "in stock",
    "Oolong Tea": "discontinued",
    "White Tea": "in stock"
}

for tea, status in tea_flavours.items():
    if status.lower() == "out of stock":
        print(f"{tea} is currently out of stock. Please check back later.")
        continue
    elif status.lower() == "discontinued":
        print(f"{tea} has been discontinued. We apologize for the inconvenience.")
        break
    else:
        print(f"{tea} is available for purchase.")

print("Thank you for visiting our tea shop!")


# Example of using else with a for loop (fallback) 
staff = [("Alice", "16"), ("Bob", "17"), ("Charlie", "17"), ("David", "19")]
for name, age in staff:
    if int(age) <= 30:
        print(f"{name} is eligible to be a manager.")
        break
else:
    print(f"No one is eligible to be a manager at this time.")