f = open('files/27_3b.txt', 'r')

n, k = map(int, f.readline().split())

s = 0
ks = 0
ms = -1010
a = [10 * 10] * k
a[0] = 0

for i in range(n):
    x = int(f.readline())
    s += x

    if x < 0 and abs(x) % 10 == 7:
        ks += 1
    r = ks % k

    if a[r] != 10 ** 10 and s - a[r] > ms:
        ms = s - a[r]

    if s < a[r]:
        a[r] = s

print(ms)
