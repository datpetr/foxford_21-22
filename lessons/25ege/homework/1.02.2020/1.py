from math import sqrt


def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


iMaxDiff = []
maxDiff = 0
count = 0

for i in range(238941, 315675 + 1):
    q = round(sqrt(i))
    D = [2] + list(range(3, q + 1, 2))
    for x in D:
        if i % x == 0 and simple(x):
            y = i // x
            if x != y and simple(y):
                count += 1
                if (y - x) > maxDiff:
                    maxDiff = y - x
                    iMaxDiff = i
                break

print(count, iMaxDiff)
