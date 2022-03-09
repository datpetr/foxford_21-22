def is_divided(x, a):
    return x % a == 0


a = 1

while True:
    for x in range(1, 1000000):
        if not ((not is_divided(x, a)) <= ((is_divided(x, 16)) <= (not is_divided(x, 24)))):
            break
    else:
        print(a)
    a += 1