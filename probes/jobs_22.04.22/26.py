# f = open('files/26.txt')
#
# n = int(f.readline())
# a = {}
#
# for _ in range(n):
#     r, p = list(map(int, f.readline().split()))
#     a[r] = a.get(r, []) + [p]
#
# for i in sorted(a.keys()):
#     count = 0
#     for j in a[i]:
#         if