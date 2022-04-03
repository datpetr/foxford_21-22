f = open('files/24_11.txt', 'r').read().splitlines()

count = 0
mx = 0

for st in f:
    s = [-1] * 100
    f = [-1] * 100
    m = 0

    for i in range(len(st)):
        if s[ord(st[i])] == -1:
            s[ord(st[i])] = i
        else:
            f[ord(st[i])] = i

    for i in range(100):
        if s[i] != -1 and f[i] != -1:
            if f[i] - s[i] > m:
                m = f[i] - s[i]

    if m > mx:
        mx = m
        count = 1
    elif m == mx:
        count += 1

print(count, mx)
