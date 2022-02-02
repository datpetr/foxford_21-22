k = []
for i in range(12, 256):
    s = bin(i)[2:]
    s = s[:1] + s[2] + s[1] + s[3:]
    s = s[:2] + s[3] + s[2] + s[4:]
    k.append(int(int(s, 2)) - i)

print(max(k))
