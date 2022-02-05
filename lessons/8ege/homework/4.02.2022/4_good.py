from itertools import permutations, product

a = set(list(permutations('ШУРУМБУРУМ', 10)))

st = ''
count = 0

for el in a:
    flag = True
    st2 = ''
    for i in range(8):
        if el[i] in ' ШРМБ' and el[i+1] in 'ШРМБ' and el[i+2] in 'ШРМБ':
            flag = False
            break

    if flag:
        count += 1

print(count)
