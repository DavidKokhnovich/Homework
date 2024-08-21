def create_phonenumber(numbers):
    phone_number = '({}{}{}){}{}{}-{}{}-{}{}'.format(*numbers)
    return phone_number

result = create_phonenumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(result)