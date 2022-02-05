from itertools import permutations

a_bad = set(list(permutations('ШРМБ', 3)))
print(list(a_bad))
for i in a_bad:
    if 'ШРМ' in a_bad:
        print('да')
