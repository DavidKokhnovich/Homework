number = int(input('Введите двузначное число: '))
if number%10 == number//10:
    print('Да, это число', number)
else:
    print('Нет')
