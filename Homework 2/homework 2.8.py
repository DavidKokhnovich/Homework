print('Стороны треугольника:')
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
if a + c > b and  a + b > c and b + c > a:
    print("Треугольник возможен")
else:
    print("Треугольник не возможен")
