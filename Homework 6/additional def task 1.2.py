def sort_of_numbers(lst):
    odd = []
    even =[]
    for num in lst:
        if num % 2:
            even.append(num)
        else:
            odd.append(num)
    return even + odd
nums = [5, 8, 6, 3, 4]
sorted_nums = sort_of_numbers(nums)
print(sorted_nums)

