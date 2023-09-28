import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(x, y):
    q.append((x,y))

    while q:
        x, y = q.popleft()

        if x == target[0] and y == target[1]:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

tc = int(input())

for i in range(tc):
    l = int(input())
    q = deque() # 🔥
    graph = [[0] * l for _ in range(l)]
    current = list(map(int, input().split()))
    target = list(map(int, input().split()))

    print(bfs(current[0], current[1]))