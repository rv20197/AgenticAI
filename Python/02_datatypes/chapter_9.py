# Set and Frozenset
essential_spices = {"salt", "pepper", "cardamom", "turmeric"}
print(f"Essential spices: {essential_spices}")
optional_spices = {"paprika", "coriander", "cardamom"}
print(f"Optional spices: {optional_spices}")

all_spices = essential_spices.union(optional_spices)
print(f"All spices: {all_spices}")

common_spices = essential_spices.intersection(optional_spices)
print(f"Common spices: {common_spices}")

unique_essential_spices = essential_spices.difference(optional_spices)
print(f"Unique essential spices: {unique_essential_spices}")

# Frozenset example
immutable_spices = frozenset(essential_spices)
print(f"Immutable spices: {immutable_spices}")