from math import sqrt


divCount = 6

for n in range(164700, 164753):
    divs = []
    q = round(sqrt(n))

    if q ** 2 == n:
        divs = [q]
        q -= 1

    for d in range(1, q + 1):
        if n % d == 0:
            divs += [d, n // d]
            if len(divs) > divCount:
                break

    if len(divs) == divCount:
        print(n, *sorted(divs))
