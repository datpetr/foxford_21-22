def simple(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


k = []
for n in range(1547341, 1547410):
    if simple(n):
        k.append(n)

print(k.sort())
