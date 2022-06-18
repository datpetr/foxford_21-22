for i in range(224466, 664423):
    if i % (5 * 7 * 13) == 0:
        if i % 25 != 0 and i % 49 != 0 and i % 169 != 0:
            m = 0
            for j in range(2, 6):
                if i % j == 0 and m == 0:
                    m = i // j
                    break

            if m % 100 == 19 and m <= 100_000:
                print(i, m)
