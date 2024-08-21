def even_numbers(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

nums = [62, 15, 36, 789, 8]
print(even_numbers(nums))