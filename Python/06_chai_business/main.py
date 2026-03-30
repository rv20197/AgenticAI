from recipes.flavours import elaichi_tea, ginger_tea
from utils.discounts import apply_discount

print(elaichi_tea())
print(ginger_tea())
original_price = 100
discounted_price = apply_discount(original_price, 20)
print(f"Original Price: ${original_price}")
print(f"Discounted Price: ${discounted_price:.2f}")