import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])
# n = 1
#     1
# n = 2
#     1 0
# n = 3
#      1 0 0
#      1 0 1
# n = 4 ->
#      1 0 1 0
#      1 0 0 0
#      1 0 1 0
# n = 5
#       1 0 1 0 0
#       1 0 1 0 1
#       1 0 0 0 0
#       1 0 0 1 0
#       1 0 0 0 1
