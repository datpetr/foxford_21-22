def if_n_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mx = 0
ans1 = 0
ans2 = 0

for num in range(631632, 684935):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num // i and if_n_simple(i) and if_n_simple(num // i):
                if (num // i) - i > mx:
                    mn = (num // i) - i
                    ans1 = i
                    ans2 = num // i

print(ans1, ans2)
