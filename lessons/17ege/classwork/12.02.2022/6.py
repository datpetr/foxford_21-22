f = list(map(int, open('files/17_6.txt', 'r').readlines()))

mx_elem = -1
mn = 100000
count = 0

for i in f:
    if i > mx_elem and i % 171 == 0:
        mx_elem = i

for i in range(len(f) - 1):
    if ((f[i] > mx_elem or f[i + 1] > mx_elem)
            and ('11' in (str(f[i])) or ('11' in str(f[i + 1])))):
        count += 1
        if (f[i] + f[i + 1]) < mn:
            mn = f[i] + f[i + 1]

print(mn, count)
