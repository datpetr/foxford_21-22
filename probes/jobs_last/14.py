n = 7 * (729 ** 543) - 6 * (81 ** 765) - 5 * (9 ** 987) - 20

count = 0

while n > 0:
    if n % 9 == 8:
        count += 1

    n //= 9

print(count)
