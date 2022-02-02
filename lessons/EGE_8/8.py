from itertools import permutations

s = sorted(list(['И', 'Н', 'С', 'Т', 'А', 'В', 'К']))
s2 = ''
k = 0
flag = True

vowels = 'ИА'
consonants = 'НСТВК'

for i in s:
    s2 += i

a = permutations(s2)
b = set(a)

for a1 in s2:
    for a2 in s2:
        for a3 in s2:
            for a4 in s2:
                if a1 in consonants and a4 in vowels and (a1 + a2 + a3 + a4) == 'НИКА':
                    print(a1 + a2 + a3 + a4)
                    print(k + 1)
                    flag = False

                if flag and a1 in consonants and a4 in vowels:
                    k += 1
