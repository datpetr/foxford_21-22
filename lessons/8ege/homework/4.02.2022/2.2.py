from itertools import permutations

a = set(list(permutations('ВЫИГРЫВАТЬ', 10)))
count = 0

for el in a:
    if el[0] != 'Ь':
        flag = True

        for i in range(9):
            if el[i] in 'ЫИА' and el[i + 1] in 'ЫИА':
                flag = False
                break

        if flag:
            count += 1

print(count)
