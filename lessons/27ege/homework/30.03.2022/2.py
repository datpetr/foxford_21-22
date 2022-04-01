f = open('files/2a.txt', 'r')

n = int(f.readline())
mn_list = [10001] * 5
s = 0

for _ in range(n):
    d = list(map(int, f.readline().split()))
    d.sort(reverse=True)
    s += d[0]

    if (d[0] - d[1]) < mn_list[(d[0] - d[1]) % 5]:
        mn_list[(d[0] - d[1]) % 5] = d[0] - d[1]

print(s, mn_list)
f.close()
