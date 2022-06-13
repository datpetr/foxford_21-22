def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = set()
n = 10 ** 7

while len(numbers) < 5:
    if is_simple(n):
        numbers.add(n)
    n -= 1

while len(numbers) < 10:
    if is_simple(n):
        numbers.add(n)
    n += 1

numbers = sorted(numbers)
for i in numbers:
    print(abs(10 ** 7 - i), i)
