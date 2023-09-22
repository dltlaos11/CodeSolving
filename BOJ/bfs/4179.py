# 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동
# 불은 각 지점에서 네 방향으로 확산
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
# 지훈은 1분에 한 칸밖에 못가지만, 불은 1분에 인접한 네 방향에 모두 퍼진다.
# input
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수
#: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.
# out
# 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
# 지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간
# 지훈이와 불의 bfs를 해야함. 매 시간 check해야
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while f_queue:
        x, y =f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or  ny < 0 or ny >= c: continue
            if f_visited[nx][ny] >= 0 or graph[nx][ny] == "#": continue
            f_visited[nx][ny] = f_visited[x][y] + 1
            f_queue.append((nx, ny))
# 여기까지
#         for j in f_visited:
#             print(j)
#         print("#####")

    while j_queue:
        x, y =j_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c: return j_visited[x][y] + 1
            if j_visited[nx][ny] >= 0 or graph[nx][ny] == "#": continue
            if f_visited[nx][ny] == -1 or f_visited[nx][ny] > j_visited[x][y] + 1: # 🔥🔥🔥🔥 아 그 저 그 수를 비교하려다 보니 이리 되었소만.. ..ㅇ잉이제 된거야..!? 이제 된거야 !? 헐 미친.. 간다..!?
                j_visited[nx][ny] = j_visited[x][y] + 1
                j_queue.append((nx, ny))

    return 'IMPOSSIBLE'

r, c = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [list(input().strip()) for _ in range(r)]
f_visited, j_visited = [[-1] * c for _ in range(r)], [[-1] * c for _ in range(r)]
f_queue, j_queue = deque(), deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == "F":
            f_queue.append((i, j))
            f_visited[i][j] = 0
        elif graph[i][j] == "J":
            j_queue.append((i, j))
            j_visited[i][j] = 0
print(bfs())
