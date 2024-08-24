def filter_string(string, lenght):
    filter_lst = list(filter(lambda x: len(x) > lenght, string))
    return filter_lst

lst = ['cat', 'word', 'hi', 'hello']
print(filter_string(lst, 3))
