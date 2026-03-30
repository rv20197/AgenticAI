def pure_chai(cups):
    return cups * 10

total_chai = 10

def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
print(f"Total chai before making {total_chai}")
impure_chai(5)
print(f"Total chai after making {total_chai}")

# Recurive function example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120


# Higher-order function example
def apply_operation(x, y, operation):
    return operation(x, y)  # Call the operation function with x and y

def add(a, b):
    return a + b

result = apply_operation(3, 4, add)
print(result)


# Lambda function example
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

tea_types = ["Green", "Black", "Oolong", "White"]
capitalized_tea_types = list(map(lambda tea: tea.lower(), tea_types))
print(capitalized_tea_types)  # Output: ['green', 'black', 'oolong', 'white']

healthy_tea_types = list(filter(lambda tea: "Green" in tea, tea_types))
print(healthy_tea_types)  # Output: ['Green']