from itertools import permutations, product

a = set(list(permutations('ШУРУМБУРУМ', 10)))
a_bad = set(list(permutations('ШРМБ', 3)))

k = []
st = ''

for i in a_bad:
    for j in i:
        st += j
    k.append(st)
    st = ''

print(k)

count = 0

for el in a:
    flag = True
    st2 = ''
    for i in range(9):
        if el[i] in 'ШРМБ':
            st2 += el[i]
            if st2 in k:
                flag = False
                break
        else:
            st2 = ''

    if flag:
        count += 1

print(count)
