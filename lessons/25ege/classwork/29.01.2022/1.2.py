def sl(n):
    a = []
    for i in range(2, n + 1):
        flag = True
        for j in range(2, int(i ** 0.5) + 1):
            if n % j == 0:
                flag = False
        if flag:
            a.append(i)
    return a


n = 100000
a = sl(n)
mx = 0
mx_n = 0

for num in range(100000, 200000 + 1):
    count = 0
    for i in a:
        if num % i == 0:
            count += 1
    if count > mx:
        mx = count
        mx_n = num

print(mx, count)