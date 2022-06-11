from functools import lru_cache


@lru_cache()
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return f(n - 2) - f(n - 1)
    if n > 2 and n % 2 != 0:
        return f(n - 2) - f(n - 3)


print(f(50))