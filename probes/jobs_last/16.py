from functools import lru_cache


@lru_cache()
def f(n):
    if n < 3:
        return n * 3
    if n > 2 and n % 2 == 0:
        return f(n - 2) * f(n - 1) - n
    if n > 2 and n % 2 != 0:
        return f(n - 1) - f(n - 2) + 2 * n


s = str(f(30))
print(s)
print(s[-2] + s[-1])
