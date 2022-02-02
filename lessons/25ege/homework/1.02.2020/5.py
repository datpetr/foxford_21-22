def simple(n):
    if n < 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


start, end = 1500000, 3000000

for num in range(3, int(end ** (1 / 6)) + 1):
    if simple(num):
        j = 1
        while (num ** 6) * j <= end:
            if start <= (num ** 6) * j <= end + 1:
                print((num ** 6) * j)
                break
            else:
                j *= 2
