def filter_words(words):
    word_5 = []
    for word in words:
        if len(word) == 5:
            word_5.append(word)
    return word_5

words = ['banana', 'house', 'apple', 'key']
print(filter_words(words))