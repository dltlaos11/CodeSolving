N, M = map(int, input().split())
visited = [False] * N
res = []

def solve(depth, N, M):
    if depth == M: 
        print(' '.join(map(str, res)))
        return
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            res.append(i+1)
            solve(depth+1, N, M)
            visited[i] = False
            res.pop()

solve(0, N, M)