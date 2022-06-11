def f(x, y):
    if x == y:
        return 1
    if x < 10:
        return 0
    return f(x // 10 + x % 10, y) + f((x // 10) * (x % 10), y)


count = 0
for i in range(10, 100):
    if f(i, 8):
        count += 1
print(count)
