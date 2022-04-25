f = list(map(int, open('files/27_1b.txt', 'r').readlines()))
n = f.pop(0)

s = s1 = s2 = ans = 0

if n % 2 == 0:
    for i in range(1, n // 2):
        s += f[i] * i + f[-i] * i
        s1 += f[i]
        s2 += f[-i]

    s += f[n // 2] * (n // 2)
    s1 += f[n // 2]
    s2 += f[0]
else:
    for i in range(1, n // 2):
        s += f[i] * i + f[-i] * i
        s1 += f[i]
        s2 += f[-i]
    s2 += f[0]

sm = s
print(s, s1, s2)

for i in range(1, n):
    s = s - s1 + s2
    s1 = s1 - f[i] + f[(n // 2 + i) % n]
    s2 = s2 + f[i] - f[(n // 2 + i) % n]
    if s < sm:
        sm = s
        ans = i

print(sm, ans + 1)
