f = open('files/24_2.txt', 'r').readline()

count = 0
k = [0] * 100

mx = 0


for i in range(len(f) - 4):
    if f[i] == f[i + 1] == 'A' and f[i + 3] == f[i + 4] == 'B':
        k[ord(f[i + 2])] += 1
        count += 1

for i in range(len(k)):
    if k[i] >= mx:
        mx = k[i]
        code_sign = i


print(count, chr(code_sign))
