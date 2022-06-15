for i in range(-64, 0):
    s = i
    s = (s + 13) * 10
    n = 512
    while s < 0:
        n = n // 2
        s = s + n

    if n == 8:
        print(i)
        break
