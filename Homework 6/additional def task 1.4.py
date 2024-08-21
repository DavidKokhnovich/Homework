def The_same_elements(list_1, list_2):
    return [elem for elem in list_1 if elem in list_2]

list_1 = [24, 17, 99, 5]
list_2 = [6, 99, 14, 24]
print(The_same_elements(list_1, list_2))
