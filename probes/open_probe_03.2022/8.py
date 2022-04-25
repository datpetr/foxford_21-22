from itertools import permutations

s = list(map(''.join, permutations('0123456789', 5)))
count = 0
k = []

for i in s:
    if i[-1] != '3' and i[-1] != '4' and i[-1] != '7':
        for j in '0123456789':
            if j * 3 in i:
                break
        else:
            count += 1
            k.append(i)

print(count)
print(k)