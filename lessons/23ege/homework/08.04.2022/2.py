def nProg(x, t):
    if x == t:
        return 1
    if x > t or x == 18:
        return 0
    return nProg(x + 1, t) + nProg(x * 2, t) + nProg(x * 3, t)


print(nProg(4, 10) * nProg(10, 34))
