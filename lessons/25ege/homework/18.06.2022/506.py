def is_simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def factors(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d.add(i)
    return sorted(d)


for i in range(25317, 51238):
    a = [j for j in factors(i) if is_simple(j)]
    if len(a) >= 6:
        print(i, max(a))