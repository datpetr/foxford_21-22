f = list(map(int, open('files/17.txt', 'r').readlines()))

mn = 100001
for i in f:
    if i < mn and i % 103 == 0:
        mn = i

count, mx_pair = 0, 0
for i in range(len(f) - 1):
    pair = f[i] + f[i + 1]
    if pair % 2 == 0 and abs(f[i] - f[i + 1]) % mn == 0:
        count += 1
        if pair > mx_pair:
            mx_pair = pair

print(count, mx_pair)
