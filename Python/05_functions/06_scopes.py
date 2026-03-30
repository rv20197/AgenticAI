def serve_chai():
    chai_type = "Masala Chai"
    print(f"Serving {chai_type} to the customer.") # local scope

chai_type = "Green Tea" # global scope
serve_chai()
print(f"The tea available in the shop is {chai_type}.") # global scope