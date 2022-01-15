import sys

a = int(sys.stdin.readline())

for i in range(a):
    c = int(sys.stdin.readline())
    dp = [1, 1, 1, 1] + [0 for j in range(c+3)]
    if c<=3:
        print(1)
    else:
        for i in range(4, c+3):
            dp[i] = dp[i-3] +dp[i-2]
        print(dp[c])