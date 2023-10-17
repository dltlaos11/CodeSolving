import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + dp[i])
print(max(dp))

# 10 -4 3 1 5 6   -35 12 21 -1
# 10  6 9 10 15 21 -14 12 33 32