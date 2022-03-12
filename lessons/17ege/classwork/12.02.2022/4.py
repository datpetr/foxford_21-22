f = list(map(int, open('files/17_4.txt', 'r').readlines()))

mx = 0
count = 0

for i in range(len(f) - 3):
    s = f[i] + f[i + 1] + f[i + 2] + f[i + 3]
    if s > mx:
        mx = s
        count = 1
    elif s == mx:
        count += 1

# for i in range(len(f) - 3):
#     s = f[i] + f[i + 1] + f[i + 2] + f[i + 3]
#     if s == mx:
#         count += 1

print(mx, count)
