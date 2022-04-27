from itertools import permutations


def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factors(num, d=2):
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            yield d
            num = n1


# n = int(input("Integer: "))
# print('{} = {}' .format(n, ' * '.join(map(str, factors(n)))))

d = list(map(''.join, permutations('34567', 5)))
for i in d:
    for j in '34567':
        if i.count(j) > 1:
            break
    else:
        if int(i) % 11 == 0:
            print(i)