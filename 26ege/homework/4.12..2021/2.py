k = []

for n in range(7548, 24659):
    if str(n)[-1] != str(oct(n)[2:])[-1]:
        if n % 13 == 0 or n % 15 == 0 or n % 17 == 0:
            k.append(n)

print(len(k), min(k))
