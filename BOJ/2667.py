import sys
from collections import deque
input = sys.stdin.readline
ans = []

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: # 범위
                continue
            if graph[nx][ny] != 1 or visited[nx][ny]:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            cnt +=1

    if cnt != 0: ans.append(cnt)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)

print(len(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])