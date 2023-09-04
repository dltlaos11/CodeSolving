# 상하좌우로 연결된 그림의 크기를 알아내기 -> 큐에서 pop을 몇 번하는지만 세면
# 도화지에 있는 모든 그림을 찾아내기 -> 현재 어떤 한 시작점 이어진 그림만 찾아내는 법만 알고있 -> 이중 for문을 돌면서 BFS의 시작점이 될 수 있는 곳을 찾기

# 1로 연결된 것을 한 그림이라고 정의
# input: 그림의 개수
# 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(x)]
graph = []
visited = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([False]*m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    init_cnt = 1 # bfs 시작시 누적 방지를 위해 1로 초기화
    queue = deque()
    queue.append((x,y)) # 소관호 튜플 - 수정이 ❌
    visited[x][y] = True # 방문

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위
                continue
            if visited[nx][ny] or graph[nx][ny] != 1: # 이미 방문했거나 그림의 영역이 아닐 경우
                continue
            visited[nx][ny] =True
            queue.append((nx, ny))
            init_cnt += 1

    return init_cnt

cnt, max_cnt = 0,0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt +=1 # 그림의 개수
            max_cnt = max(max_cnt, bfs(i,j))
print(cnt)
print(max_cnt)
