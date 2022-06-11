f = list(map(int, open('files/17.txt', 'r').readlines()))

count_pairs = 0
mx_pair = 0
mn_numb = 10000 + 1

for i in f:
    if i % 17 == 0 and i < mn_numb:
        mn_numb = i


for i in range(len(f) - 1):
    if f[i] % mn_numb == 0 or f[i + 1] % mn_numb == 0:
        count_pairs += 1
        if f[i] + f[i + 1] > mx_pair:
            mx_pair = f[i] + f[i + 1]


print(count_pairs, mx_pair)
