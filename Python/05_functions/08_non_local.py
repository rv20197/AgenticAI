def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type # Accessing variable from it's parent's scope
        chai_type = "Masala"
    kitchen()

    print(f"Chai type is {chai_type}")

update_order()