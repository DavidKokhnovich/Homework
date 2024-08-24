def Even_numbers(lst):
    res = [n for n in lst if n % 2 == 0]
    return res
lst = [3, 62, 4, 9, 21]
print(Even_numbers(lst))
