N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)