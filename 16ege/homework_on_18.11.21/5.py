def F(n):
    if n == 20:
        return 262144
    elif n > 20:
        return F(n-1) - G(n-1)


def G(n):
    if n == 20:
        return -262144
    elif n > 20:
        return G(n-1) - F(n-1)


print(G(34))
