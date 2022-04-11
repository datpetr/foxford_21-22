from functools import lru_cache


@lru_cache()
def f(x, t):
    if x == t:
        return 1
    elif x > t:
        return 0
    return f(x + 2, t) + f(x * 2, t)


print(f(1, 16) * f(16, 52))
