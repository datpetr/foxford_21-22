from itertools import permutations

a = set(list(permutations('ШУРУМБУРУМ', 10)))
a_bad = set(list(permutations('ШРМБ', 3)))
count = 0

for el in a:
    flag = True

    for i in range(9):
        if el[i] == 'У' and el[i + 1] == 'У':
            flag = False
            break

    if flag:
        count += 1

print(count)
