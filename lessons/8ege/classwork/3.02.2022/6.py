from itertools import permutations

a = set(list(permutations('КУКУРУЗА')))
count = 0

for el in a:
    flag = True

    for i in range(7):
        if el[i] in 'УА' and el[i + 1] in 'УА':
            flag = False

    if flag:
        count += 1

print(count)
