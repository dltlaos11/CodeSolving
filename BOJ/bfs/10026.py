import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(map(str, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
q = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 같은 색, 방문 ❌
            if 0<= nx <n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = 1
                q.append((nx, ny))

# 적록색약 ❌
res1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            res1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]

res2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            res2 += 1

print(res1, res2)