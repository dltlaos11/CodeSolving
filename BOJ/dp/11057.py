import sys

input = sys.stdin.readline

n = int(input())
dp = [1]*10 # n이 1자릿 수 일 떄 dp 세팅
for i in range(1,n) : # 수의 길이 1 ~9
    for j in range(1,10) : # 맨 뒷자리

        dp[j] += dp[j-1]
        # print(dp[j], dp[0]) # dp가 3일 떄 기존의 dp[1,1,1, ... 1,1] 2번 실행

print(sum(dp)%10007)