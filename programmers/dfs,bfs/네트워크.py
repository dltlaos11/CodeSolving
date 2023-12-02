from collections import deque
# 인접행렬 [[1, 1, 0], [1, 1, 0], [0, 0, 1]] 연결 유무 A-B,B-A | 그래프를 코드로 표현하는 방식
# 인접리스트
def solution(n, computers):
    answer = 0
    visited = [False] * n
    queue = deque()
    
    def bfs(start):
        visited[start] = True
        queue.append(start)
        
        while queue:
            v = queue.popleft()
            # print(v, visited)
            
            for i in range(n):
                # 방문하지 않은 연결된 컴퓨터를 visited에 check후, 기반으로 
                # computers의 모든 컴퓨터 조회(방문하지 않은 컴퓨터 중 연결된 컴퓨터)
                if computers[v][i] == 1 and not visited[i]:
                    # 새로운 정점의 visited 처리
                    # 한번에 visited 모두 check되면 1, 아니면 전체 for문의 i만큼 돌면서 더해줌
                    # 방문하지 않은은 것 중 방문한게 있다면 더해주지 않고 계속 visited 체크
                    print(v, i, "방문하지 않은 연결된 컴퓨터")
                    visited[i] = True
                    queue.append(i)

    # 방문하지 않은 컴퓨터 중 작은 번호부터 BFS
    for i in range(n):
        if not visited[i]:
            # 방문하지 않은 컴퓨터 중 연결된 컴퓨터가 없다면 순회하며 check
            print(visited, i)
            bfs(i)
            answer += 1
            print(visited, i)
    
    return answer

# from collections import deque

# def solution(n, computers):
    
#     def bfs(x, y):
#         q.append((x,y))
#         visited[x][y] = True

#         while q:
#             x,y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 # if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and computers[nx][ny] == computers[x][y]:
#                 if 0 <= nx < n and 0 <= ny < n and computers[nx][ny] == 1 and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     q.append((nx, ny))
    
#     answer = 0
    
#     visited = [[False] * n for _ in range(n)]
#     q = deque()
    
#     dx = [1,0,-1,0]
#     dy = [0,1,0,-1]
    
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j] and computers[i][j] == 1:
#             # if not visited[i][j]:
#                 bfs(i, j)
#                 answer += 1
    
#     # print(visited)
    
#     return answer