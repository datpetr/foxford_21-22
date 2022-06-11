a = []

for i in range(3000):
    n = 1024
    s = i
    while s >= 5:
        s -= 5
        n //= 2
    if n == 64:
        a.append(i)

print(max(a))