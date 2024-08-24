a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
ab = range(a, b+1)
lias_ab = [n for n in ab if n % 2 == 0]
print(lias_ab)
