def f(x, pos, p, v):  # prev +1 -- 1; +2 -- 2; x * 2 -- 3
    if x >= 21 and (pos == 3 or pos == 5):  # или x >= 21 and (pos == 1 or pos == 3): (1)
        return True
    elif x < 21 and pos == 5:  # или x x < 21 and pos == 3: (2); (1) и (2) должны выполняться вместе потом откидываем
        # совпадения в двух вариациях
        return False
    elif x >= 21 and (pos == 2 or pos == 4):
        return False

    if pos % 2 == 0:
        if p == 1:
            return f(x + 2, pos + 1, 2, v) or f(x * 2, pos + 1, 3, v)
        if p == 2:
            return f(x + 1, pos + 1, 1, v) or f(x * 2, pos + 1, 3, v)
        if p == 3:
            return f(x + 1, pos + 1, 1, v) or f(x + 2, pos + 1, 2, v)
        else:
            return f(x + 2, pos + 1, 2, v) or f(x * 2, pos + 1, 3, v) or f(x + 1, pos + 1, 1, v)
    else:
        if v == 1:
            return f(x + 2, pos + 1, p, 2) and f(x * 2, pos + 1, p, 3)
        if v == 2:
            return f(x + 1, pos + 1, p, 1) and f(x * 2, pos + 1, p, 3)
        if v == 3:
            return f(x + 1, pos + 1, p, 1) and f(x + 2, pos + 1, p, 2)
        else:
            return f(x + 2, pos + 1, p, 2) and f(x * 2, pos + 1, p, 3) and f(x + 1, pos + 1, p, 1)


for s in range(1, 21):
    if f(s, 0, 0, 0):
        print(s)
