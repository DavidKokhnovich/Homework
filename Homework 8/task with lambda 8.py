def numbers_division_by_three(nums):
    return list(filter(lambda x: x % 3 == 0, nums))

nums = [62, 15, 36, 789, 8]
print(numbers_division_by_three(nums))