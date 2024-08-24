def sum_of_numbers(num):
    i = 0
    for n in str(num):
        i += int(n) ** 2

    return i

print(sum_of_numbers(321))