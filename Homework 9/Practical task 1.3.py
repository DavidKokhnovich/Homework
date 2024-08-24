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
    if y < 0 or y > 100 or y < 0 or y > 100:
        return (0, 0)
    return (x, y)


compass_direction = input("Введите Букву S,W,E,N: ")

for i in compass_direction:
    if i in 'SWEN':
        res = compass(compass_direction)

print(res)