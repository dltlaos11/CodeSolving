import sys
input = sys.stdin.readline
# 시간초과 해결해줌

a, b = map(int, input().split())

val = list(map(int, input().split()))
for i in range(a-1):
    val[i+1] += val[i]
val = [0] + val

for _ in range(b):
    c, d = map(int, input().split())
    print(val[d] - val[c-1])