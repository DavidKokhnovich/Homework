string = input("Строка:")
vowels = "а","у","о","и","э","ы","я","ю","е","ё","a","e","i","o","u","y","А","У","О","И","Э","Ы","Я","Ю","Е","Ё","A","E","I","O","U","Y"
vowel_count = 0

for symbol in string:
    if symbol in vowels:
        vowel_count += 1
print(string, vowel_count)
print('Программа завершена')