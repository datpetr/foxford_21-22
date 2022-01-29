def if_n_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mn = 10000000
ans1 = 0
ans2 = 0

for num in range(523426, 578926):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num // i and if_n_simple(i) and if_n_simple(num // i):
                if (num // i) - i < mn:
                    mn = (num // i) - i
                    ans1 = i
                    ans2 = num // i

print(ans1, ans2)
