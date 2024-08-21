def filter_list(I):
    lst = []
    for i in I:
        if type(i) != str:
            lst.append(i)
    return lst

print(filter_list(['cat', 1, 24, 'beaver', 7]))
