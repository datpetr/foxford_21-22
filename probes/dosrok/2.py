print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not (x <= z)) or (y == w) or (not y))
                if not f:
                    print(x, y, z, w, f)