from itertools import permutations

a = list(permutations('СЧИТАЙ', 4))
count = 0
print(len(a))
for i in a:
    if i.count('А') <= 1:
        count += 1

print(count)
