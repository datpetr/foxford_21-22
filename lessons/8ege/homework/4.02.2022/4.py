from itertools import permutations, product

a = set(list(permutations('ШУРУМБУРУМ', 10)))
a_bad = set(list(permutations('ШРМБ', 3)))

k = []
st = ''
count = 0

for i in a_bad:
    for j in i:
        st += j
    k.append(st)
    st = ''

print(k)

for el in a:
    flag = True
    st2 = ''
    for i in range(10):
        if el[i] in 'ШРМБ':
            st2 += el[i]
            if st2 in k or len(st2) >= 3:
                flag = False
                break
        else:
            st2 = ''

    if flag:
        print(el, end=' ')
        count += 1

print(count)
