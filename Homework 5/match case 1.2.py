day = input("Введите день недели: ")

match day:
    case 'Saturday':
        print('Выходной')
    case 'Sunday':
        print('Выходной')
    case _:
        print('рабочий')
