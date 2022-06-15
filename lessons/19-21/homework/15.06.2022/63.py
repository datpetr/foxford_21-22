def f(a, b, c, m):
    if a + b >= 80:
        return c % 2 == m % 2

    if c == m:
        return 0

    h = [f(a + b, b, c + 1, m), f(a, a + b, c + 1, m)]

    return any(h) if c % 2 != m % 2 else all(h)


for s in range(1, 30):
    for m in range(1, 5):
        if f(20, s, 0, m):
            if m == 3:
                print(s, m)
            break
