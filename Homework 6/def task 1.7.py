def words_with_e(array):
    with_e = 'e'
    new_list = []
    for words in array:
        if with_e in words:
            new_list.append(words)
    return new_list

array = ["hedgehog", "banana", "bear", "door"]
print(words_with_e(array))
