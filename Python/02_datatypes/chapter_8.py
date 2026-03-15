ingredients = ["water", "tea leaves", "milk", "cardamom", "ginger"]
print(f"Ingredients list: {ingredients}")
ingredients.append("sugar")
print(f"Ingredients after adding sugar: {ingredients}")

ingredients.remove("ginger")
print(f"Ingredients after removing ginger: {ingredients}")

ingredients.insert(2, "black tea")
print(f"Ingredients after inserting black tea: {ingredients}")

ingredients.sort()
print(f"Sorted ingredients: {ingredients}")

ingredients.reverse()
print(f"Reversed ingredients: {ingredients}")

chai_ingredients = ingredients.copy()
print(f"Copied ingredients list: {chai_ingredients}")

chai_ingredients.extend(["cinnamon", "cloves"])
print(f"Chai ingredients after extending: {chai_ingredients}")

ingredients.pop()
print(f"Ingredients after popping the last item: {ingredients}")

ingredients.clear()
print(f"Ingredients after clearing the list: {ingredients}")


sugar_levels = [1, 2, 3, 4, 5]
print(f"Sugar levels: {sugar_levels}")

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
print(f"Total sugar level: {sum(sugar_levels)}")