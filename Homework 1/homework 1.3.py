k = 3666
hour = k // 3600
minute = (k-(hour*3600)) // 60
second = k-hour*3600-minute*60
print(hour,':',minute,':',second)