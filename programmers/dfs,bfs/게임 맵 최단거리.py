from collections import deque
def solution(maps):
    answer = 0
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    queue = deque()
    
    def bfs(x, y):
        cnt = -1
        queue.append((x,y))
        visited[x][y] = True
        while queue:
            x, y = queue.popleft()
            
            if x == n-1 and y == m-1:
                cnt = maps[n-1][m-1]
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y]+1
        return cnt
    
    answer =bfs(0,0)
    
    return answer