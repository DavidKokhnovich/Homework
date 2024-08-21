print('Стороны треугольника:')
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
if a == b or b == c or a == c:
    print('Равнобедренный')
elif a == b == c:
    print('Равносторонний')
else:
    print('Разносторонний')
    