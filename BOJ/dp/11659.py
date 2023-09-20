# 누적합
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
pre_sum = [0]

tmp = 0
for i in arr:
    tmp += i
    pre_sum.append(tmp)

for i in range(n):
    a, b = map(int, input().split())
    print(pre_sum[b] - pre_sum[a - 1])
