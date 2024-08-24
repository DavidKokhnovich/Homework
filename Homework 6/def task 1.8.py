def positive_numbers(num):
    for i in num:
        if i <= 0:
            return False
    return True
num = [700, 23, -14]
num_1 = [700, 23, 14]
print(positive_numbers(num))
print(positive_numbers(num_1))
