f = list(map(int, open('files/17.txt').readlines()))

count, mx_pair, sum_numbers = 0, 0, 0
for i in f:
    if i > 0:
        sum_numbers += int(str(i)[0])
    else:
        sum_numbers += int(str(i)[1:][0])

for i in range(len(f) - 1):
    if f[i] * f[i + 1] > sum_numbers:
        count += 1
        pair = f[i] + f[i + 1]
        if pair > mx_pair:
            mx_pair = pair

print(count, mx_pair)
