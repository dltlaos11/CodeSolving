import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int,input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == -1:
                    continue
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y]+1
                    q.append((nz, nx, ny))
bfs()
res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            res = max(res, graph[i][j][k])
print(res-1) 