print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not (y <= w)) or (x == z) or x)
                if not f:
                    print(x, y, z, w, f)