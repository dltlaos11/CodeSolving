from collections import deque

def solution(board):
    answer = 0
    graph = board
    visited = [[False] * len(board) for i in range(len(board))]

    dx = [0, -1, 0, 1, -1, 1, 1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()
            visited[x][y] = True

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(board) and 0 <= ny < len(board):
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        visited[nx][ny] = True

    for i in range(len(board)):
        for j in range(len(board)):
            if graph[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)

    cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if graph[i][j] == 0:
                cnt += 1
    return cnt
