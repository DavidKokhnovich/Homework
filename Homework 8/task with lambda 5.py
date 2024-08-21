def filter_string(lst):
    filter_lst = list(filter(lambda x: x[0].lower() == 'a', lst))
    return filter_lst

lst = ['cat', 'word', 'hi', 'hello', 'apple', 'Anna']
print(filter_string(lst))