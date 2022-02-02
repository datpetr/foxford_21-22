def simple(n):
    if n < 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


start, end = 1000000, 2000000

for num in range(int((start // 2) ** 0.25) , int((end // 2) ** 0.25) + 1):
    if simple(num):
        print(2 * num ** 4)
