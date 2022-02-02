f = open("files/24_5.txt").readlines()

_max = 0
counter = 0

for s in f:
    last_max = 0
    for c in range(26):
        p1 = s.find(chr(c + ord('A')))
        p2 = s.rfind(chr(c + ord('A')))
        last_max = max(last_max, p2 - p1 + 1)
    if _max == last_max:
        counter += 1
    elif _max < last_max:
        counter = 1
        _max = last_max

print(counter, _max - 1)
