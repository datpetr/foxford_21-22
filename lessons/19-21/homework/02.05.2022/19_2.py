def f(x, y, pos):
    if x + y >= 38 and pos == 2:
        return True
    elif x + y < 38 and pos == 2:
        return False
    elif x + y >= 38 and pos == 1:
        return False

    if pos % 2 != 0:
        return (f(x + 2, y, pos + 1) or f(x + y, y, pos + 1)
                or f(x, y + 2, pos + 1) or f(x, x + y, pos + 1))
    else:
        return (f(x + 2, y, pos + 1) and f(x + y, y, pos + 1)
                and f(x, y + 2, pos + 1) and f(x, x + y, pos + 1))


for s in range(1, 15):
    if f(8, s, 0):
        print(s)
        break
