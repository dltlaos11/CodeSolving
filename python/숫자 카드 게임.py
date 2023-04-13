# 행, 열 : N, M
# 행마다 작은값.. 결국엔 각 행들중 작은값의 리스트들 중에서 가장 큰값이 정답이다.
N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)