# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
# 각각의 로프에는 모두 고르게 w / k 만큼의 중량
# 각 로프들에 대한 정보가 주어졌을 때,
# 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성

# 내림차순 최대 중량,

import sys
input = sys.stdin.readline

n = int(input())

k = [int(input()) for _ in range(n)]

k.sort(reverse=True)

res = []
# maxW = rope[0]

for i in range(n):
    res.append(k[i]*(i+1))
print(max(res))

# for i in range(1, n):
#     if maxW < rope[i] * (i+1):
#         maxW = rope[i] * (i+1)

# 정당성 판별