print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x == y) or ((y or z) <= x)
            if not f:
                print(x, y, z, f)
