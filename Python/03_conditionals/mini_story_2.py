snacks = ["cookies","samosas"]

snack_input = input("What snack do you want? ")

if snack_input.lower() in snacks:
    print("Here you go!")
else:
    print("Sorry, we don't have that snack.")