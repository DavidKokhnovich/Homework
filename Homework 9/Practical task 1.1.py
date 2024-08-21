def compass(compass_direction):
    x, y = 0, 0
    for i in compass_direction:
        if i == 'S':
            y -= 1
        elif i == 'N':
            y += 1
        elif i == 'W':
            x -= 1
        elif i == 'E':
            x += 1
        else:
            return "Error"
    return (x, y)

compass_direction = 'SSWE'
res = compass(compass_direction)
print(res)
