from itertools import product


def f(n):
    x = str(n)
    for i in range(len(x) - 2):
        if not(x[i] != x[i + 1] and
               x[i] != x[i + 2] and
               x[i + 1] != x[i + 2]):
            return False
    return True


a = list(map(int, map(''.join, product('012345678', repeat=7))))
numbers = '347'
count = 0
for elem in a:
    if str(elem)[-1] not in numbers and f(elem):
        count += 1

print(count)
