def dict_creator(products, count):
    res = {}
    for item in range(len(products)):
        res[products[item]] = count[item]
    return res

products = ['apple', 'milk', 'orange']
count = [1, 3, 12]

print(dict_creator(products, count))

