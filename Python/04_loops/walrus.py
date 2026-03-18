# value = 13
# remainder = value % 5

# if remainder == 0:
#     print(f"{value} is divisible by 5.")

value = 13 
if (remainder := value % 5):
    print(f"{value} is not divisible by 5 as remainder is {remainder}.")

available_sizes = ["Small", "Medium", "Large"]

if (requested_size := input("Enter you desired size: ")) in available_sizes:
    print(f"{requested_size} is available.")
else:
    print(f"{requested_size} is not available.")

print(f"Requested size is {requested_size}.")


tea_flavours = ["Green", "Black", "Oolong", "White"]
print("Available tea flavours:")
for flavour in tea_flavours:
    print(f"- {flavour}")

while (requested_flavour := input("Enter your desired tea flavour: ")) not in tea_flavours:
    print(f"{requested_flavour} is not available. Please choose from the available flavours.")
print(f"Requested tea flavour is {requested_flavour}.")