import sys

input = sys.stdin.readline

TC = int(input())

dp = [0 for i in range(20)] # dp배열 먼저 선언
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(TC):
    N = int(input())
    for i in range(4, N+1): # for문 돌면서 초기값을 넣어주는 것이 안정적
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[N])

# DP의 두가지 방법
# Tabulation (bottom up)
# 하향식 -> dp, 0부터 tabulation
# Memoization (top down)
# 상향식 -> 재귀, 마지막이 1일 떄까지

# TC = int(input())
# dp = dp = [0]*(1001)
# dp[0] = 1
#
# for i in range(TC):
#     n = int(input())
#     for i in range(1,n+1):
#         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#     print(dp[n])

# dp = dp = [0]*(10)
# dp[0] =1
# dp[9]=9
# dp[8]=8
# for i in range(1, 5):
#     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
#     print(dp, "dp")
#     print(dp[i-2], "dp[i-2]")
#     print(dp[i - 3], "dp[i-3]")