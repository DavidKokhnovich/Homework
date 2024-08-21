a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
ab = range(a, b+1)
a_b = [n ** 2 for n in ab]
print(a_b)

