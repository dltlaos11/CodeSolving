# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)
# 걷거나 순간이동
# 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다
# 1초 후에 2*X
#  동생은 점 K(0 ≤ K ≤ 100,000)
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n)
    # 방문처리가 필요
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            break

        for i in (x-1,x+1,x*2):
            if i < 0 or i > max:
                continue
            if visited[i]:
                continue
            visited[i] = visited[x] +1
            queue.append(i)
    # while q:
    #     cur = q.pop()
    #     for nx in (cur-1, cur+1, cur*2):
    #         if nx < 0 or nx >= maxSize:
    #             continue
    #         if arr[nx] != -1:
    #             continue
    #
    #         arr[nx] = arr[cur] + 1
    #         q.appendleft(nx)

max = 100000
n,k = map(int,input().split())
visited = [0] * (max+1)
bfs()

# 5
# 10(순간이동)
# 9(걷기)
# 18(순간이동)
# 17(걷기)