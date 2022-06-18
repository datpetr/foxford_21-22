from collections import Counter


f = list(map(int, open('files/17.txt').readlines()))

ch = [sum(map(int, str(x))) for a, x, c in zip(f, f[1:], f[2:])
      if sum(map(int, str(a))) == sum(map(int, str(c)))]

print(len(ch), Counter(ch).most_common()[0][0])
