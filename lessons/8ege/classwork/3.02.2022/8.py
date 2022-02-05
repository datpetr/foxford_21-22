from itertools import permutations

a = set(list(permutations('ФОТОЭФФЕКТ', 10)))
count = 0

for el in a:
    flag = True

    for i in range(9):
        if el[i] in 'ОЭЕ' and el[i + 1] in 'ОЭЕ':
            flag = False

    if flag:
        count += 1

print(count)
