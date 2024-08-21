def square_numbers(nums):
    square = list(map(lambda x: x ** 2, nums))
    return square

nums = [62, 15, 36, 79, 8]
print(square_numbers(nums))