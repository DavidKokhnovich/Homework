def palindrom(num):
    return str(num) == str(num)[::-1]

def check_palindrom(number):
    less_than_a_palindrom = number - 1
    more_than_a_palindrom = number + 1
    while True:
        if palindrom(less_than_a_palindrom):
            return less_than_a_palindrom
        elif palindrom(more_than_a_palindrom):
            return more_than_a_palindrom
        else:
            less_than_a_palindrom -= 1
            more_than_a_palindrom += 1

print(check_palindrom(188))