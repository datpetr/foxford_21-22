def SumDig(n):
    sd = 0
    while n > 0:
        sd += (n % 10)
        n //= 10
    return sd


f = list(map(int, open('files/17_8.txt', 'r').readlines()))

s_35 = -1
mn = 100000
count = 0

for i in f:
    if i % 35 == 0:
        s_35 += SumDig(i)

for i in range(len(f) - 1):
    if ((f[i] > s_35 >= f[i + 1] and hex(f[i + 1])[-1] == 'f' and hex(f[i + 1])[-2] == 'e')
            or (f[i + 1] > s_35 >= f[i] and hex(f[i])[-1] == 'f' and hex(f[i])[-2] == 'e')):
        count += 1
        if (f[i] + f[i + 1]) < mn:
            mn = f[i] + f[i + 1]

print(mn, count)
