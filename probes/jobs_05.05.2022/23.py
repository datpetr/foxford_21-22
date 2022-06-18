def nProg(a, b, y):
    if a + b == y:
        return 1
    if a + b > y:
        return 0
    return nProg(a + b, b, y) + nProg(a, a + b, y)


print(nProg(1, 1, 88))
