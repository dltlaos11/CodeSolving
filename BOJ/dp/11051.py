N, K = map(int, input().split())
# dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp = [[1 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, K+1):
    for j in range(i+1, N+1):
        dp[j][i] = dp[j - 1][i - 1] + dp[j - 1][i]
        # if i == j:
        #     dp[i][j] = 1
        # elif j==0:
        #     dp[i][j] = 1 #2C1 = 1C0 + 1C1 -> dp = [[1 for _ in range(K+1)] for _ in range(N+1)]



# 5C2, dp[4][1]+dp[4][2]
# dp[0][0], dp[0][1], dp[0][2]
# ❌❌❌❌❌❌❌❌❌❌❌ yeah
# 1C1,
# 2C1, 2C2,
# 3C1, 3C2
# 4C1, 4C2
# 5C1, 5C2
# 1이요
print(dp[N][K] % 10007)