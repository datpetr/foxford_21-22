def F(n):
    global s
    s += 2 * n + 1
    if n > 1:
        s += 3 * n - 8
        F(n - 1)
        F(n - 4)


for i in range(3, 1000):
    s = 0
    F(i)
    if s > 5000000:
        print(i, s)
        break
