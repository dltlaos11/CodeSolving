# N, M = map(int, input().split())
# visited = [False] * N
# res = []
#
# def solve(depth, idx, N, M):
#     if depth == M:
#         print(' '.join(map(str, res)))
#         return
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             res.append(i+1)
#             solve(depth+1, i+1, N, M)
#             visited[i] = False
#             res.pop()
# solve(0, 0, N, M)

from itertools import combinations

n, m = map(int,input().split())
arr = [i for i in range(1, n+1)]
res = list(combinations(arr, m))
for i in res:
    for j in i:
        print(j, end=' ')
    print()