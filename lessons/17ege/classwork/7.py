def simple(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


k = 0
mx = 0

for i in range(50000, 100001):
    for j in range(2, round(i ** 0.5) + 1):
        if i % j == 0:
            if simple(i) and simple(i // j):
                k += 1
                mx = i


print(k, mx)
