def dell(n, m):
    return n % m == 0


count = 0

for a in range(-1000, 1000):
    if a == 0:
        continue
    for x in range(1, 1000):
        if not(dell(a, 25) and ((dell(x, 24) and dell(x, 75)) <= dell(x, a))):
            break
    else:
        count += 1

print(count)