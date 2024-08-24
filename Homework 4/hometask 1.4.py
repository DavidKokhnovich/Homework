def the_smallest_common_multiple(a, b):
    c = max(a, b)

    while True:
        if c % a == 0 and c % b == 0:
            the_smallest_common_multiple = c
            break
        c += 1
    return the_smallest_common_multiple

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
res = the_smallest_common_multiple(a, b)
print(f'Наименьшее общее кратное для чисел {a} и {b} составляет: {res}')