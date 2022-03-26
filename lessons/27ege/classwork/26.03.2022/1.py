def simple(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


f = open('files/27_1b.txt', 'r')
n = int(f.readline())

s = 0
ks = 0
a = [0] * 9
ms = 0

for i in range(n):
    x = int(f.readline())
    s += x

    if simple(x):
        ks += 1
    r = ks % 9

    if a[r] != 0 and (s - a[r]) > ms:
        ms = s - a[r]

    if a[r] == 0:
        a[r] = s

print(ms)
