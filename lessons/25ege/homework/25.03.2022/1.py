def f(n):
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i != i:
                a.append(n // i)
                a.append(i)
            else:
                a.append(i)
    a.sort()
    return a


num = 500000001
count = 0

while count < 5:
    a_func = f(num)
    sum_ = 0
    if len(a_func) >= 3:
        s = a_func[-1] + a_func[-2] + a_func[-3]

        for i in str(s):
            sum_ += int(i)

        if sum_ == 33:
            print(s, a_func[-1], num)
            count += 1
    num += 1
