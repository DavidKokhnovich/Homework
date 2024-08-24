month = 7
months = {1: 'январе', 2: 'феврале', 3: 'марте', 4: 'апреле', 5: 'мае', 6: 'июне', 7: 'июле', 8: 'августе', 9: 'сентябре', 10: 'октябре', 11: 'ноябре', 12: 'декабре'}
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print(f'Вы родились в {months[month]}. За окном падал белый снег.')
elif month in spring:
    print(f'Вы родились в {months[month]}. Птицы пели прекрасные песни.')
elif month in summer:
    print(f'Вы родились в {months[month]}. Солнце светило ярче чем когда-либо.')
else:
    print(f'Вы родились в {months[month]}. Урожай был невероятным.')
