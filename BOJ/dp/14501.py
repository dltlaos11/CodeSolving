# i=0
# 0~8
# 3~8
# 0
# dp[3] = dp[0]+sc[0][1] 10
# dp[4] = dp[0]+sc[0][1] 10
# dp[5] = dp[0]+sc[0][1] 10
# dp[6] = dp[0]+sc[0][1] 10
# dp[7] = dp[0]+sc[0][1] 10
# 1
# 6~8
# dp[6] = dp[1] + sc[1][1] 20
# dp[7] = dp[1] + sc[1][1] 20
# dp[8] = dp[1] + sc[1][1] 20
# 2
# 3~8
# dp[3] = dp[2] + sc[2][1]
# dp[3] = dp[2] + sc[2][1]
# dp[3] = dp[2] + sc[2][1]
# dp[3] = dp[2] + sc[2][1]
# 3
# 4~8
# dp[4] = dp[3] + sc[3][1] 30
# dp[5] = dp[3] + sc[3][1] 30
# dp[6] = dp[3] + sc[3][1] 30
# dp[7] = dp[3] + sc[3][1] 30
# 4
# 6~8
# dp[6] = dp[4] + sc[4][1] 45
# dp[7] = dp[4] + sc[4][1] 45
# dp[8] = dp[4] + sc[4][1] 45
# 5
#
import sys
# Dynamic Programming은 큰 문제를 작은 부분 문제로 나누고,
# 그 작은 부분문제들이 반복되는 것을 이용하여 풀어가는 방법
# 모든 작은 문제들을 단 한 번만 풀어야 하며, 그 결과를 어딘가 기록해 둠으로써 재사용
# 부분 문제를 푸는 순서에 따라서 Top-Down과 Bottom-up

# Bottom-up
n = int(input())

schedule = [list(map(int, input().split())) for i in range(n)]

dp = [0 for i in range(n+1)]

for i in range(n): # "i번째까지 일했을 때 얻는 최대 수익"을 계산하기 위한 i
    for j in range(i+schedule[i][0], n+1): # j는 i번째 날에 상담을 진행했을 때, "상담이 가능한 모든 날짜", 즉 i + "상담 기간"부터 마지막 날까지
        if dp[j] < dp[i] + schedule[i][1]: # j를 기준으로 상담을 진행했었을 때 얻는 최대 수익을 dp[j]에 저장
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])

# Top-Down

# N = int(input())
# li = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(N+1)]
#
# for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 ❌
#     if i + li[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
#         dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])
#
# print(dp[0])