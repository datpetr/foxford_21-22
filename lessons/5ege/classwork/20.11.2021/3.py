for i in range(6, 1000):
    s = i
    s = (s + 3) // 9
    n = 45
    while s < 2021:
        s *= 2
        n += 5
    if n == 75:
        print(i)
        break
