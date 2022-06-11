count = 0
for i in range(-10000, 10000):
    s = i
    s *= 10
    n = 3
    while s > 0:
        s -= n
        n *= 2
    if n == 768:
        count += 1

print(count)