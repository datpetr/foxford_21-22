from itertools import product


def f(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return False
    return True


a = list(map(''.join, product('АЕЖЙМУ', repeat=5)))

pos = count = 0
for elem in a:
    pos += 1
    if pos % 2 == 0 and f(elem):
        count += 1

print(count)
