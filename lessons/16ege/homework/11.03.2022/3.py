from functools import lru_cache


@lru_cache()
def Fr(n):
    if n <= 1:
        return 2 * n + 1
    return 2 * n + 1 + 3 * n - 8 + Fr(n - 1) + Fr(n - 4)


x = 0
while 1:
    x += 1
    sm = Fr(x)
    if sm > 5000000:
        print(x, sm)
        break
