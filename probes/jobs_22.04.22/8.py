from itertools import product


def f(x):
    for i in range(len(x) - 1):
        if x[i] == x[i + 1]:
            return False
    return True


a = list(map(''.join, product('АЕПСТУХ', repeat=4)))

count, pos = 0, 0
for elem in a:
    pos += 1
    if pos > 1000 and f(elem):
        count += 1

print(count)
