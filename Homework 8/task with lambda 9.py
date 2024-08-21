def numbers_in_range(nums):
    return list(filter(lambda x: x in range(5, 10), nums))

nums = [62, 15, 36, 789, 8, 5]
print(numbers_in_range(nums))