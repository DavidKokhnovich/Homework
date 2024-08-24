def taxi(km, min_cost, price_per_km):
    if km <= 3:
        cost = min_cost
    else:
        cost = min_cost + price_per_km * (km-3)
    return cost

km = 17.5
min_cost = 2.0
price_per_km = 0.3
print(taxi(km, min_cost, price_per_km))