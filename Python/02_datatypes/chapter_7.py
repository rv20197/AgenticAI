# Tuples and Membership Testing

masala_spices = ("cumin", "turmeric", "coriander", "cardamom")
print(f"Masala spices: {masala_spices}")

# Accessing elements in a tuple
first_spice = masala_spices[0]
print(f"The first spice in the masala is: {first_spice}")

# Unpacking a tuple
(spice1, spice2, spice3, spice4) = masala_spices
print(f"Spices unpacked: {spice1}, {spice2}, {spice3}, {spice4}")

ginger_ratio, cardamom_ratio = 1,2
print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping - Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

#  Membership testing
if "cumin" in masala_spices:
    print("Cumin is part of the masala spices.")

if "black pepper" not in masala_spices:
    print("Black pepper is not part of the masala spices.")