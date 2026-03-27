def add_vat(price, vat_rate):
    """
    Calculate the price including VAT.

    Parameters:
    price (float): The original price of the item.
    vat_rate (float): The VAT rate as a percentage (e.g., 20 for 20%).

    Returns:
    float: The price including VAT.
    """
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    return total_price

# Example usage:
original_price = 100.0
vat_percentage = 10.0
final_price = add_vat(original_price, vat_percentage)
print(f"The price including VAT is: {final_price}")