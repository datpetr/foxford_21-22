from itertools import permutations

a = set(list(permutations('АБРАКАДАБРА', 8)))
count = 0

for el in a:
    flag = True

    for i in range(7):
        if (el[i] == 'А' and el[i + 1] == 'А') or (el[i] in 'БРКД' and el[i + 1] in 'БРКД'):
            flag = False

    if flag:
        count += 1

print(count)
