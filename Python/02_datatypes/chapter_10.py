# Dictionary
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change their contents after creation.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
person["profession"] = "Engineer"  # Adding a new key-value pair
person["age"] = 31  # Updating an existing key-value pair
print(f"Person: {person}")

chai_order = dict(tea="chai", milk="whole", sugar="2 tsp")
print(f"Chai order: {chai_order}")

# Accessing values
print(f"Name: {person['name']}")
print(f"City: {person.get('city')}")  # Using get() method
print(f"Profession: {person.get('profession', 'Not specified')}")  # Using get() with default value

# Removing items
del person["city"]  # Removing a key-value pair
print(f"Person after removing city: {person}")