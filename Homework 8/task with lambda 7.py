def filter_string(lst):
    filter_lst = list(filter(lambda x: x.isupper(), lst))
    return filter_lst

lst = ['CAT', 'word', 'HI', 'hello', 'apple', 'Anna', 'MISHA']
print(filter_string(lst))