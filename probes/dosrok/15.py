def dell(x, a):
    return x % a == 0


a = 1
while True:
    for x in range(1, 10000):
        if not(((dell(x, 3)) <= (not dell(x, 5))) or ((x + a) >= 70)):
            break
    else:
        print(a)
        break
    a += 1