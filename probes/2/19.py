def f(x, y, h):
    if x + y >= 120 and h == 2:
        return True
    else:
        if x + y < 120 and h == 2:
            return False
    return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x + 3, y, h + 1) or \
           f(x, y + 1, h + 1) or f(x, y * 2, h + 1) or f(x, y + 3, h + 1)


for s in range(1, 111):
    if f(9, s, 1):
        print(s)
        break
