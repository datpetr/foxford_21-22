count = 0

for a1 in 'BDF':
    for a2 in 'ABC':
        for a3 in '13579BDF':
            for a4 in '2468ABC':
                for a5 in '13579BDF':
                    for a6 in '2468ABC':
                        for a7 in '13579BDF':
                            for a8 in '2468ABC':
                                for a9 in '13579BDF':
                                    for a10 in '2468ABC':
                                        for a11 in '13579BDF':
                                            for a12 in '2468ABC':
                                                st = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12
                                                if a1 > a2 > a3 > a4 > a5 > a6 > a7 > a8 > a9 > a10 > a11 > a12:
                                                    count += 1

print(count)
