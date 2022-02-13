print('x y z w f')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x or ((not y) or z or (not w)) and (y or (not z))
                if not f:
                    print(x, y, z, w, f)