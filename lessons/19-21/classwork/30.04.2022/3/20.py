def f(x, pos, p, v):  # prev +1 -- 1; +2 -- 2; x * 2 -- 3
    if x >= 21 and (pos == 2 or pos == 4):
        return True
    elif x < 21 and pos == 4:
        return False
    elif x >= 21 and (pos == 1 or pos == 3):
        return False

    if pos % 2 != 0:
        if v == 1:
            return f(x + 2, pos + 1, p, 2) or f(x * 2, pos + 1, p, 3)
        if v == 2:
            return f(x + 1, pos + 1, p, 1) or f(x * 2, pos + 1, p, 3)
        if v == 3:
            return f(x + 1, pos + 1, p, 1) or f(x + 2, pos + 1, p, 2)
        else:
            return f(x + 2, pos + 1, p, 2) or f(x * 2, pos + 1, p, 3) or f(x + 1, pos + 1, p, 1)
    else:
        if p == 1:
            return f(x + 2, pos + 1, 2, v) and f(x * 2, pos + 1, 3, v)
        if p == 2:
            return f(x + 1, pos + 1, 1, v) and f(x * 2, pos + 1, 3, v)
        if p == 3:
            return f(x + 1, pos + 1, 1, v) and f(x + 2, pos + 1, 2, v)
        else:
            return f(x + 2, pos + 1, 2, v) and f(x * 2, pos + 1, 3, v) and f(x + 1, pos + 1, 1, v)


for s in range(1, 21):
    if f(s, 0, 0, 0):
        print(s)
