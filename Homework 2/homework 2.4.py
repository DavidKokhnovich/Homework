a = 283691
b = a%10
a = a//10
while a > 0:
    if a%10 > b:
     b = a%10
    a = a//10
print(b)
