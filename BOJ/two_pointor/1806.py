import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
sum = arr[0]
ans = 100001 # 길이

while True:
    if sum >= s:
        sum -= arr[left]
        ans = min(ans, right - left + 1)
        left += 1
    else:
        right += 1
        if right == n:
            break
        sum += arr[right]

print(0) if ans == 100001 else print(ans)
