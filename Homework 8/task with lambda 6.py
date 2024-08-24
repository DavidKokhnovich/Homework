def filter_nums(nums):
    filter_lst = list(filter(lambda x: x > 10, nums))
    return filter_lst

nums = [62, 10, 15, 36, 789, 8]
print(filter_nums(nums))