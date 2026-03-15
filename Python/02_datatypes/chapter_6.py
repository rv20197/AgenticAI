chai_type = "Ginger Tea"
customer_name = "Alice"
print(f"Welcome to our tea shop, {customer_name}!")
print(f"Today's special is: {chai_type}")

chai_description = "A warm and soothing tea with a blend of ginger and spices."
print(f"Description: {chai_description}")

# Indexing the chai description
first_word = chai_description[0:6]  # This will extract the first word "A warm"
print(f"The first word of the description is: '{first_word}'")

# Slicing the chai description
last_word = chai_description[-4:]  # This will extract the last word "spices."
print(f"The last word of the description is: '{last_word}'")

# Reverse the chai description
reversed_description = chai_description[::-1]
print(f"Reversed description: '{reversed_description}'")

label_text = "Chai Spēcial"
encoded_label = label_text.encode('utf-8')
decoded_label = encoded_label.decode('utf-8')
print(f"Original label: {label_text}")
print(f"Encoded label: {encoded_label}")
print(f"Decoded label: {decoded_label}")