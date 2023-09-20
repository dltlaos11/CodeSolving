# X가 3으로 나누어 떨어지면, 3으로 나눈다
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 위 3가지의 연산을 활용해 1을 만드는 데 최소연산횟수
# out
# 연산의 최소 횟수
# 둘째줄: N을 1로 만드는 방법에 포함되어있는 수를 공백으로 구분해서 출력

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001

for i in range(2, n + 1):

    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
res = [n]
now = n
temp = dp[n] - 1 # 14, 17번째 에서 1을 더하기 직전의 값을 찾아내기 위해서 추적하기 위한 temp

for i in range(n, 0, -1):

    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):

        now = i # 값
        res.append(i)
        temp -= 1 # 다음 값을 찾기 위해서 -1

print(*res)


# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
# dp = [0 for _ in range(n+1)]
#
# for i in range(1,n+1):
#     dp[i] = dp[i-1]+numbers[i-1]
#
# for i in range(m):
#     start,end = map(int, input().split())
#     print(dp[end]-dp[start-1])
