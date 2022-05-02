def f(x, y, pos):
    if x + y >= 71 and pos == 2:
        return True
    elif x + y < 71 and pos == 2:
        return False
    elif x + y >= 71 and pos == 1:
        return False

    if pos % 2 != 0:
        return f(x + 3, y, pos + 1) or f(x * 2, y, pos + 1) or f(x, y + 3, pos + 1) or f(x, y * 2, pos + 1)
    else:
        return f(x + 3, y, pos + 1) and f(x * 2, y, pos + 1) and f(x, y + 3, pos + 1) and f(x, y * 2, pos + 1)


for s in range(1, 57):
    if f(13, s, 0):
        print(s)
        break
