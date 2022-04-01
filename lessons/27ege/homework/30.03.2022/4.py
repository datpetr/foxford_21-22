f = open('files/4b.txt', 'r')

n = int(f.readline())
mx_list = [10000001] * 11
s = 0

for _ in range(n):
    d = list(map(int, f.readline().split()))
    d.sort(reverse=True)
    s += d[2]

    if (d[0] - d[1]) < mx_list[(d[0] - d[1]) % 11]:
        mx_list[(d[0] - d[1]) % 11] = d[0] - d[1]
    if (d[0] - d[2]) < mx_list[(d[0] - d[2]) % 11]:
        mx_list[(d[0] - d[2]) % 11] = d[0] - d[2]

if s % 11 == 0:
    print(s)
else:
    print(s, mx_list)
    print(mx_list[11 - s % 11])
    print(11 - s % 11)
f.close()
