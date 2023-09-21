import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = list(map(int, input().split()))

left = 0
right = 0

sum = a[0]

cnt = 0

while True:
    if sum == m:
        sum -= a[left]
        left +=1
        cnt +=1
    if sum < m:
        right += 1
        if right == n:
            break
        sum += a[right]
    if sum > m:
        sum -= a[left]
        left += 1
print(cnt)