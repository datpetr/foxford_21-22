# n = 36
# dp = [0] * (n + 2)
#
# dp[10] = 1
#
# for i in range(11, 18):
#     if (i // 2) * 2 == i:
#         dp[i] = dp[i // 2] + dp[i - 2] + dp[i - 3]
#     else:
#         dp[i] = dp[i - 2] + dp[i - 3]
#
# print(dp)
#
# for i in range(17):
#     dp[i] = 0
#
# print(dp)
#
# for i in range(18, n + 1):
#     if (i // 2) * 2 == i:
#         dp[i] = dp[i // 2] + dp[i - 2] + dp[i - 3]
#     else:
#         dp[i] = dp[i - 2] + dp[i - 3]
#
# print(dp)

def nProg(x, t):
    if x == t:
        return 1
    if x > t:
        return 0
    return nProg(x + 3, t) + nProg(x + 2, t) + nProg(x * 2, t)


print(nProg(10, 18) * nProg(18, 36))
