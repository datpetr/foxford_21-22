n = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404
n = abs(n)
count = 0

while n:
    if n % 5 == 2:
        count += 1
    n //= 5

print(count)