def make_chai():
    return "tea", "milk", "sugar"

returned_values = make_chai()
print(returned_values)

def idle_tea():
    pass

print(idle_tea())

def sold_cups():
    return 5

print(sold_cups())

def chai_status(cups_left):
    if cups_left == 0:
        return "Chai is not available"

    return "Chai is available"

print(chai_status(5))
print(chai_status(0))

def chai_report():
    cups_left = 5
    status = chai_status(cups_left)
    return status, cups_left

print(chai_report())