def simple(n):
    if n < 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


start, end = 1000000, 5000000

for num in range(int((start // 2) ** 0.25) , int((end // 2) ** 0.25) + 1):
    if simple(num):
        print(2 * num ** 4, 2, 2 * num, 2 * num ** 2, 2 * num ** 3, 2 * num ** 4)
        print(2 * num ** 4, 1, num, num ** 2, num ** 3, num ** 4)
