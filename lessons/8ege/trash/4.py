from itertools import permutations


a = permutations('ФОКСИК')
b = set(a)
k = 0

for c in b:
    w = ''.join(c)
    if w.count("ОИ") > 0 or w.count("ИО") > 0:
        k += 1

print(len(b) - k)
