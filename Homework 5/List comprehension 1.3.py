array = input('Введите строку:')
vowels = 'eyuioa'
list_array = [letter for letter in array if letter in vowels]
print(list_array)