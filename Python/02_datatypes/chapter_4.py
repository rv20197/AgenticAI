# Boolean
is_boiling = True
print(f"Is the tea boiling? {is_boiling}.")
is_freezing = False
print(f"Is the ice freezing? {is_freezing}.")

stir_count = 5

total_actions = stir_count + is_boiling # In Python, True is treated as 1 and False as 0 when used in arithmetic operations (upcasting). 
print(f"Total actions (stirs + boiling state): {total_actions}.")

milk_present = 0
tea_present = 1
print(f"Is milk present? {bool(milk_present)}.")
print(f"Is tea present? {bool(tea_present)}.")

# Logical operations
is_tea_ready = is_boiling and tea_present
print(f"Is tea ready? {bool(is_tea_ready)}.")

is_tea_ready_or_milk_present = is_boiling or milk_present
print(f"Is tea ready or is milk present? {bool(is_tea_ready_or_milk_present)}.")

