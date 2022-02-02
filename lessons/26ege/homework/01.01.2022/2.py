n = 20

t1 = 9
t2 = 7
t3 = 5

l = 0
r = 20 * 5

while r - l > 1:
    mid = (r + l) // 2
    if (mid // t1 + mid // t2 + mid // t3) < n:
        l = mid
    else:
        r = mid

print(l, r)
