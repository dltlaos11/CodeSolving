from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    start_x, start_y = find_R(n, m, board)
    
    return bfs(start_x, start_y, n, m, board)

def find_R(n, m, board):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return i, j

def bfs(start_x, start_y, n, m, board):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        if board[x][y] == 'G':
            return moves
        
        for dx, dy in directions:
            new_x, new_y = x, y
            
            # 한 방향으로 끝까지 미끄러지기
            while True:
                next_x = new_x + dx
                next_y = new_y + dy
                
                if (not (0 <= next_x < n and 0 <= next_y < m) or 
                    board[next_x][next_y] == 'D'):
                    break
                
                new_x, new_y = next_x, next_y
            
            if not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, moves + 1))
    
    return -1