number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите приблизительную сумму первых двух чисел: "))
if number1+number2>number3:
    print('Меньше')
elif number1+number2<number3:
    print('Больше')
else:
    print('Равно')
