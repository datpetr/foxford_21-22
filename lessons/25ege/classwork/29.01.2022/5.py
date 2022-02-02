def if_n_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mn = 1000000
ans = 0
a = []

for num in range(412567, 473265):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i ** 2 != num and if_n_simple(i) and if_n_simple(num // i):
                a.append(num)

print(len(a))
sr = sum(a) / len(a)
print(sr)

for i in a:
    if abs(i - sr) < mn:
        mnn = abs(i - sr)
        ans = i

print(ans)
