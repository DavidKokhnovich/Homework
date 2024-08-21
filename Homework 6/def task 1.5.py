def filter_words(words):
    res = [word for word in words if word.startswith('a')]
    return res

words = ["banana", "aplle", "human", "autumn"]
print(filter_words(words))