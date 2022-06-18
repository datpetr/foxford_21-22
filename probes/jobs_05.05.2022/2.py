print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a <= b) and (c <= d) or (not c))
                if not f:
                    print(a, b, c, d, f)