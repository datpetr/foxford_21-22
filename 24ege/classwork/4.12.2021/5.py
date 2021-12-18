f = open('files/24_5.txt', 'r')
st = f.readline()

s = ''
count = 0
mx = 0

print(s)

while st:
    s = [-1] * 100
    k = [-1] * 100
    for i in range((len(st))):
        if s[ord(st[i])] == -1:
            s[ord(st[i])] = i
        else:
            k[ord(st[i])] = i
    for i in range(100):
        if s[i] != -1 and k[i] != 1:
            if k[i] - s[i] > mx:
                m = k[i] - s[i]

    if m > mx:
        mx = m
        count = 1
    elif m == mx:
        count += 1
    st = f.readline()

print(mx, count)
f.close()