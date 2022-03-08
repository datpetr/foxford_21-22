with open("files/4a.txt") as f:
    n = int(f.readline())
    s = 0
    min_diff = 10001

    for i in range(n):
        x = sorted(list(map(int, f.readline().split())))
        s += x[2]
        diff1 = x[2] - x[1]
        diff2 = x[2] - x[0]
        min_diff = min(min_diff, (diff1 if diff1 % 11 else 10001), (diff2 if diff2 % 11 else 10001))

    if s % 11 == 0:
        print(s)
    else:
        print(s - min_diff)
        print(s)
