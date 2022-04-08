from functools import lru_cache


@lru_cache()
def nProg(x, t):
    if x == t:
        return 1
    if x > t or x == 21:
        return 0
    return nProg(x + 1, t) + nProg(x * 3, t) + nProg(x * 4, t)


print(nProg(2, 16) * nProg(16, 65))
