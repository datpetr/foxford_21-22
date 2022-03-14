def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(4542345, 4542419):
    if simple(i):
        print(i)
