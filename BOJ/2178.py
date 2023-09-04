import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
visited = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
    visited.append([-1]*m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위
                continue
            if visited[nx][ny] >= 0 or graph[nx][ny] != 1: # 이미 방문했거나 그림의 영역이 아닐 경우
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))
    return visited[n-1][m-1] + 1

print(bfs(0,0))