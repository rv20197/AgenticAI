def chai_counter():
    chai_order = "Lemon tea" # Enclosing Scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner order is {chai_order}")
    print_order()
    print(f"Outer Order is {chai_order}")

chai_order = "Masala Tea"
print(f"Global Chai Order: {chai_order}")
chai_counter()