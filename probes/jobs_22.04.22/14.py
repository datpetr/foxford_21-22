a = set()
for x in range(4019):

    n = 3 * (16 ** 2018) - 2 * (8 ** 1028) - 3 * (4 ** 1100) - 4 ** x - 2022
    sum_ranks = 0

    while n:
        sum_ranks += x % 4
        n //= 4

    a.add(sum_ranks)

print(a)
print(len(a))
