import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # if a < 0 or a >= n or b <0 or b >= m: continue
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
bfs()
res = 0
for i in graph:
    for j in i:
        if j==0: # -1로 감싸있는 경우
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)

