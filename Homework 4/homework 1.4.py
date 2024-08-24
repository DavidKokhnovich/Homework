num = int(input("Введите число n:"))
my_list = list(range(1, num))
i = 0
a_list = []

while i < len(my_list):
    if my_list[i] % 2 == 0:
        a_list.append(my_list[i])
    i += 2
    print(i)
print('Программа завершена')
