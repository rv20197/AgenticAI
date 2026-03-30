chai = "Ginger Tea"

def prepare_chai(order):
    print(f"Preparing {order}")

chai = [1,2,3]
prepare_chai(chai)


def edit_tea(cup):
    cup[1] = 42

edit_tea(chai)

print(f"Tea cups {chai}")

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling", "Yes","Low")


def special_tea(*ingredients,**extras):
    print(f"Ingredients {ingredients}")
    print(f"Extras {extras}")

special_tea("Cinnamon","Elaichi", sweetner="Honey", foam="yes")

def chai_order(order=None):
    if order is None:
        order = []
        order.append("Chai")
    print(order)

chai_order("Green Tea")
chai_order()
