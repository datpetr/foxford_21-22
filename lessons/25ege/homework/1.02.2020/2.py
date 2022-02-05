def simple(n):
    if n < 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


start, end = 247264322, 369757523

for num in range(int(start ** 0.25) + 1, int(end ** 0.25) + 1):
    if simple(num):
        print(num ** 4, num ** 3)
