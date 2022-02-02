def simple(n):
    sm = True
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            sm = False
            break
    return sm


k = []


for num in range(5555, 7777 + 1):
    d = 0

    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0 and simple(i) and simple(num // i) and i % 10 == 3 and (num // i) % 10 == 3:
            d += 2

    if d == 2:
        k.append(num)



print(len(k), max(k))
