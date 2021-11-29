f = list(map(int, open('files/17_5.txt', 'r').readlines()))

count = 0
mx_el = 0
mn = 200001

for i in f:
    if i % 19 == 0 and i > mx_el:
        mx_el = i

for i in range(len(f) - 1):
    if f[i] > mx_el or f[i + 1] > mx_el:
        count += 1
        if f[i] + f[i + 1] < mn:
            mn = f[i] + f[i + 1]

print(count, mn)
