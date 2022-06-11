# f = open('files/24.txt', 'r').readline()
#
# subsequence_ac = ['A', 'C']
# subsequence_ab = ['A', 'B']
#
# mx = count = count_ac = count_ab = 0
#
# for i in range(len(f) - 1):
#     if f[i] == subsequence_ac[count_ac % 2]:
#         count_ac += 1
#         count += 1
#         if count > mx:
#             mx = count
#     elif f[i] == subsequence_ac[count_ac % 2]:
#         count_ab += 1
#         count += 1
#         if count > mx:
#             mx = count
#     else:
#         count = count_ab = count_ac = 0
#
# print(mx)
f = open('files/24.txt', 'r').readline()

a = mx = k = 0

for i in range(len(f)):
    if f[i] == 'A':
        a = 1
    if a == 1 and (f[i] == 'B' or f[i] == 'C'):
        k += 1