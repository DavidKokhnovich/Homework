def sums_of_square (lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num ** 2
    return sum

lst = [2, 4, 3, 23, 6]
print(sums_of_square(lst))