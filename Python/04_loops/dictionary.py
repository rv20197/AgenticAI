users = [
    {
        "name": "John Doe",
        "total_spent": 30,
        "coupon_code": "SAVE10"
    },
    {
        "name": "Jane Smith",
        "total_spent": 50,
        "coupon_code": "SAVE20"
    },
    {    
        "name": "Doe",
        "total_spent": 100,
        "coupon_code": "SAVE30"
    }
]

discounts = {
    "SAVE10": (10,0),
    "SAVE20": (20,0),
    "SAVE30": (30,0)
}

for user in users:
    percent,fixed = discounts.get(user["coupon_code"], (0, 0))
    discount_amount = (user["total_spent"] * percent / 100) + fixed
    final_amount = user["total_spent"] - discount_amount
    print(f"{user['name']} has a total of ${user['total_spent']:.2f} and receives a discount of ${discount_amount:.2f}, making the final amount ${final_amount:.2f}.")