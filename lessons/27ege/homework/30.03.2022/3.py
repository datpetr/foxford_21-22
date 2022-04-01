f = open('files/3a.txt', 'r')

n = int(f.readline())
mn_list = [10001] * 8
s = 0

for _ in range(n):
    d = list(map(int, f.readline().split()))
    d.sort(reverse=True)
    s += d[0]

    if (d[0] - d[1]) < mn_list[(d[0] - d[1]) % 8]:
        mn_list[(d[0] - d[1]) % 8] = d[0] - d[1]
    if (d[0] - d[2]) < mn_list[(d[0] - d[2]) % 8]:
        mn_list[(d[0] - d[2]) % 8] = d[0] - d[2]

print(s, mn_list)
if s % 8 == 0:
    print(s)
else:
    print(s - mn_list[s % 8])
f.close()
