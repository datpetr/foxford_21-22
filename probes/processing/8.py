from itertools import permutations


a = sorted(list(map(''.join, permutations('СОЛНЦЕ', 5))))

print(a)