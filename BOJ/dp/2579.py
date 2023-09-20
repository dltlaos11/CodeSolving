# 1 10
# 2 20
# 4 25
# 6 20
# 1 or 2 계단씩 오를 수 있음
# 시작점은 계단에 포함 ❌,
# 마지막 계단은 무조건 밟아야
# out -> 계단에서 얻을 수 있는 총 점수의 최댓값
# i번째 계단의 최댓값
import sys
input = sys.stdin.readline

n = int(input())

stair = [0]*301
for i in range(n):
    stair[i] = int(input())

dp = [0]*301
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2]+stair[i])
# 연속*(i-1:전,i:현재, dp[i-3]번째 까지의 최댓값), 불연속
print(dp[n-1])


# import sys
# input = sys.stdin.readline
#
# n: int = int(input())
# dp = [0 for _ in range(301)]
# steps = [0 for _ in range(301)]
# for i in range(n):
#     steps[i+1] = int(input())
#
# dp[1] = steps[1]
# dp[2] = steps[1] + steps[2]
#
#
# for i in range(3, n+1):
#     dp[i] = max(steps[i]+dp[i-2], steps[i]+steps[i-1]+dp[i-3])
#
# print(dp[n])