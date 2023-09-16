import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[0] * M for _ in range(N)] # graph 불필요
visited = [[False] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = []

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >=N or ny< 0 or ny >= M:
                continue
            if graph[nx][ny] != 0 or visited[nx][ny]: # graph[nx][ny] != 0 불필요
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1

    return cnt

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == False: # graph 불필요
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')
# print(*size) 배열 출력 용이