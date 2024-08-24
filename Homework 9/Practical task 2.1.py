def Checking_the_cost(money, shopping_cart):
    cost_shopping_cart = 0
    for item in shopping_cart:
        cost_shopping_cart += item['quantity'] * item['cost_item']
        money = float(money)
    if cost_shopping_cart <= money:
        return {"status": "success",
                "comment": "Покупки оплачены"}
    else:
        return {"status": "fail",
                "comment": f"Недостаточно средств." f"Внесите {round(cost_shopping_cart-money, 2)} сумму денег"}

shopping_cart = [{"name": "milk", "quantity": 2, "cost_item": 1.79},
                 {"name": "chips", "quantity": 1, "cost_item": 4.69},
                 {"name": "chocolate", "quantity": 1, "cost_item": 3.29}]
money = 10
result = Checking_the_cost(money, shopping_cart)
print(result)
