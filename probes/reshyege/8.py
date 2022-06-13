count = 0

for s1 in 'ЗИМА':
    for s2 in 'ЗИМА':
        for s3 in 'ЗИМА':
            for s4 in 'ЗИМА':
                for s5 in 'ЗИМА':
                    s = s1 + s2 + s3 + s4 + s5

                    if (s.count('И') == 1 and s.count('А') == 0) \
                            or (s.count('И') == 0 and s.count('А') == 1):
                        count += 1

print(count)