def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


# Example usage
cups_ordered = 3
price_per_cup = 2.5
total_bill = calculate_bill(cups_ordered, price_per_cup)
print(f"Total bill for {cups_ordered} cups: ${total_bill:.2f}")