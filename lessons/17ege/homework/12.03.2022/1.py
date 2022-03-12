f = list(map(int, open('1.txt', 'r').readlines()))

sum_odd = 0
sum_even = 0
count_odd = 0
count_even = 0
average_odd = 0
average_even = 0
count = 0
mx = 0
flag = True

for i in f:
    if i % 2 == 0:
        sum_even += i
        count_even += 1
    else:
        sum_odd += i
        count_odd += 1

average_even = sum_even / count_even
average_odd = sum_odd / count_odd

if average_odd > average_even:
    flag = False

if flag:
    for i in range(len(f) - 1):
        if average_odd < (f[i] + f[i + 1]) < average_even:
            count += 1
            if f[i] + f[i + 1] > mx:
                mx = f[i] + f[i + 1]
else:
    for i in range(len(f) - 1):
        if average_even < (f[i] + f[i + 1]) < average_odd:
            count += 1
            if f[i] + f[i + 1] > mx:
                mx = f[i] + f[i + 1]

print(count, mx)
