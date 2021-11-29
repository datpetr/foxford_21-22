def F(n):
    if n == 1:
        return 1
    if n == 20:
        return 262144
    else:
        return F(n - 1) - G(n - 1)


def G(n):
    if n == 1:
        return 0
    if n == 20:
        return -262144
    else:
        return G(n - 1) - F(n - 1)


print(G(34))
