lst_1 = [52, 34, 46, 71]
lst_2 = [71, 85, 34, 45]
res = [i for i in lst_1+lst_2 if i not in lst_1 or i not in lst_2]
print(res)