import sys
from collections import deque

def dfs (n):
    visited[n] = True
    print(n, end= ' ')
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] =True

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# 작은값 부터
for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)

dfs(V)

print()

visited = [False] * (N+1)

bfs(V)