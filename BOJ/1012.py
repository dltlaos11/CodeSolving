import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

TC = int(input())

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= N or ny >= M:
          continue

      if graph[nx][ny] == 1:
          queue.append((nx, ny))
          graph[nx][ny] = 0

for _ in range(TC):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# t = int(input())
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def bfs(x: int, y: int):
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 2
#
#     while q:
#         cur = q.pop()
#         for i in range(4):
#             nx = cur[0] + dx[i]
#             ny = cur[1] + dy[i]
#             if nx < 0 or nx >= m or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] != 1:
#                 continue
#             graph[nx][ny] = 2
#             q.appendleft((nx, ny))
#
#
# for i in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[0 for _ in range(n)] for _ in range(m)]
#     cnt = 0
#     for j in range(k):
#         x, y = map(int, input().split())
#         graph[x][y] = 1
#
#     for x in range(m):
#         for y in range(n):
#             if graph[x][y] == 1:
#                 cnt += 1
#                 bfs(x, y)
#
#     print(cnt)