for i in range(200, 1900):
    x = i
    L = 2 * x - 15
    M = 2 * x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 45:
        print(i)
        break