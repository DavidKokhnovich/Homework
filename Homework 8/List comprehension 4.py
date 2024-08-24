lst = range(1, 11)
res = [x**3 if x**3 % 4 !=0 else "FOUR" for x in lst]
print(res)