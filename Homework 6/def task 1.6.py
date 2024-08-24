def number_in_range(lst):
    number = []
    for n in lst:
        if n in range(11, 20):
               number.append(n)
    return number

lst_2 = [2, 16, 13, 64, 27, 20, 12]
print(number_in_range(lst_2))
