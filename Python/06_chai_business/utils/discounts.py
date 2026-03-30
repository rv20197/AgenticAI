def apply_discount(amount, discount):
    """Apply a discount to the given amount."""
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    return amount * (1 - discount / 100)