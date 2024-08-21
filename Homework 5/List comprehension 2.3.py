words1 = 'is2 Thi1s T4est 3a'
words2 = []
words3 = [words2.append(w) for i in range(1, 10) for w in words1.split() if str(i) in w]
print(' '.join(words2))
