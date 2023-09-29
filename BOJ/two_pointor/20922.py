import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))

left, right = 0, 0

counter = [0] * (max(a) + 1) # 값의 분포를 나타내기 위해 최대 크기만큼의 배열 만들기

res = 0
while right < n:
    if counter[a[right]] < k:
        counter[a[right]] += 1
        right += 1
    else:
        counter[a[left]] -= 1
        left += 1
        # 5 left
        # 4 7
        # [0, 0, 0, 0, 2, 1, 1, 0]
    res = max(res, right - left)
print(res)

