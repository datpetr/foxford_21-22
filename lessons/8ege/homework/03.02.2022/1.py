from itertools import permutations

a = set(list(permutations('СЧИТАЙ', 4)))

count = 0

for i in a:
    if i.count('A') <= 1:
        print(i)
        count += 1

print(count)
