from math import sqrt


divCount = 5

for n in range(904528, 997438):
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
        print(*sorted(divs))
