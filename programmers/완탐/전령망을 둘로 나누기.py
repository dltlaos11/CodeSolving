from collections import deque
def solution(n, wires):
    res = 0
    graph = [[] for _ in range(n+1)]
    for a,b in wires: # 정점 간선과의 관계(e.g. (a,b) 서로 graph에 더하기)
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start):
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt
            
    res = n
    for a,b in wires:
        graph[a].remove(b) # 짜르기
        graph[b].remove(a)
        res = min(abs(bfs(a) - bfs(b)), res)
        
        # 원점
        graph[a].append(b)
        graph[b].append(a)
    
    return res