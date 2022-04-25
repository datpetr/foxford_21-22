f = list(map(int, open('files/27_1b.txt', 'r').readlines()))
n = f.pop(0)

s = 0
mn = 10 ** 10
paragraph_ind = 0

for p in range(n):
    s = 0
    for i in range(n):
        d = min(abs(i - p), n - abs(i - p))
        s += f[i] * d

    if s < mn:
        mn = s
        paragraph_ind = p

print(paragraph_ind + 1, mn)
