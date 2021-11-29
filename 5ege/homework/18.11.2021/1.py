for i in range(1, 1000):
    N = i
    if N % 4 == 0:
        N = N // 2
    else:
        N -= 1
    if N % 5 == 0:
        N = N // 5
    else:
        N -= 1
    if N % 3 == 0:
        N = N // 3
    else:
        N -= 1
    if N == 3:
        print(i)
