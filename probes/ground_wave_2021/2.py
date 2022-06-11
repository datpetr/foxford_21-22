print('a b c d f')

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((not a) and (not b) or (b == c) or d)
                if not f:
                    print(a, b, c, d, f)
