def f(x, pos, prev):  # prev +1 -- 1; +2 -- 2; x * 2 -- 3
    if x >= 43 and pos == 2:
        return True
    elif x < 43 and pos == 2:
        return False
    elif x >= 43 and pos == 1:
        return False

    if pos % 2 != 0:
        if prev == 1:
            return f(x + 2, pos + 1, 2) or f(x * 2, pos + 1, 3)
        if prev == 2:
            return f(x + 1, pos + 1, 1) or f(x * 2, pos + 1, 3)
        if prev == 3:
            return f(x + 1, pos + 1, 1) or f(x + 2, pos + 1, 2)
        else:
            return f(x + 2, pos + 1, 2) or f(x * 2, pos + 1, 3) or f(x + 1, pos + 1, 1)
    else:
        if prev == 1:
            return f(x + 2, pos + 1, 2) and f(x * 2, pos + 1, 3)
        if prev == 2:
            return f(x + 1, pos + 1, 1) and f(x * 2, pos + 1, 3)
        if prev == 3:
            return f(x + 1, pos + 1, 1) and f(x + 2, pos + 1, 2)
        else:
            return f(x + 2, pos + 1, 2) and f(x * 2, pos + 1, 3) and f(x + 1, pos + 1, 1)


for s in range(1, 43):
    if f(s, 0, 0):
        print(s)
