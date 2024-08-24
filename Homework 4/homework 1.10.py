my_word = input('Введите слово:')
my_word_with_a = my_word.replace("a","")
for letter in my_word_with_a:
    print(letter)
print('Программа завершена')