# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성
# input
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# out
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력
# ------------------
# dp[i] = 2 x i
# dp[0] = 2 x 0 = 1
# dp[1] = 2 x 1 = 2
# dp[2] = 2 x 2 = 4
# dp[3] = 2 x 3 = 6
# dp[4] = 2 x 4 = 8
# dp[5] = 2 x 5 = 10 ❌
# -------------------
# 가장 왼쪽을 2x1로 덮을경우 남은건 2 x n-1 -> 남은 부분 채우는 dp[n-1],
# 가장 왼쪽을 1x2로 덮을경우 남은건 2 x n-2 -> 남은 부분 채우는 dp[n-2]
# dp[n] = dp[n-1] + dp[n-2]
# dp[1]= 1
# dp[2] = 2

import sys
input = sys.stdin.readline
n = int(input())
# dp = [0 for _ in range(n+1)] ❌
dp = [0] * 1001
dp[1]= 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])

# n: int = int(input())
#
# dp = [0 for _ in range(n+1)]
#
# for i in range(1, n+1):
#     if i == 1:
#         dp[1] = 1
#     elif i == 2:
#         dp[2] = 2
#     else:
#         dp[i] = (dp[i-1]+dp[i-2]) % 10_007
#
# print(dp[n])