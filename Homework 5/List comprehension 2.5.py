s = [3, 102, 5, 45, 94]
print([n ** 2 for n in s])
print([n % 11 for n in s])
print([n for n in s if n % 2 == 0])
print([n for n in s if len(str(n)) % 2 != 0])
print([n for n in s if n % 3 == 0])

