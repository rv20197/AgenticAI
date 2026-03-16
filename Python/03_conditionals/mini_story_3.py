cup_sizes = {
    "small": 10,
    "medium": 15,
    "large": 20
}

print("Welcome to the coffee shop!")
size_input = input("What size of coffee would you like? (small, medium, large) ")

if size_input.lower() in cup_sizes:
    print(f"Great choice! A {size_input} coffee will be {cup_sizes[size_input.lower()]} rupees.")
else:
    print("Sorry, we don't have that size. Please choose small, medium, or large.")