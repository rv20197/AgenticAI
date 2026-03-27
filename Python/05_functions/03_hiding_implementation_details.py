def get_input():
    customer_name = input("Enter customer name: ")
    tea_type = input("Enter tea type: ")
    return customer_name, tea_type

def validate_input(customer_name, tea_type):
    if not customer_name:
        raise ValueError("Customer name cannot be empty.")
    if tea_type not in ["Green Tea", "Black Tea", "Oolong Tea"]:
        raise ValueError("Invalid tea type. Must be 'Green Tea', 'Black Tea', or 'Oolong Tea'.")

    return customer_name, tea_type

def save_to_database(customer_name, tea_type):
    # Simulate saving to a database
    print(f"Saving order for {customer_name}: {tea_type} to database...")

def register_order():
    try:
        customer_name, tea_type = get_input()
        customer_name, tea_type = validate_input(customer_name, tea_type)
        save_to_database(customer_name, tea_type)
        print("Order registered successfully!")
    except ValueError as e:
        print(f"Error: {e}")

register_order()