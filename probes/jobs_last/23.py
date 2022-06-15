def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0

    return f(x - 3, y) + f(x // 2, y)


print(f(108, 42) * f(42, 12))