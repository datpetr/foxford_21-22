k = []
for i in range(1, 2000):
    x = i
    l = 0
    m = 0
    while x > 0:
        m += 1
        if x % 2 != 0:
            l += x % 8
        x //= 8
    if l == 2 and m == 3:
        k.append(i)
print(max(k))
