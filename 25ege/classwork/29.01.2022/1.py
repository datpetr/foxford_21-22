def if_n_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mx_n = 0
count_mx = 0
count = 0

for num in range(100000, 200001):
    count = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i != num // i:
                if if_n_simple(i):
                    count += 1
                if if_n_simple(num // i):
                    count += 1
        else:
            if if_n_simple(i):
                count += 1
    if count >= count_mx:
        count_mx = count
        mx_n = num

print(mx_n, count_mx)
