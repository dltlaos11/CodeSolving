# 총 F층으로 이루어짐
# 스타트링크 위치: G
# 강호가 있는 위치: S
# U: 위로 U층 이동, D: 아래로 D층 -> S - G
# G층에 도착하려면 몇 번의 버튼을 눌러야 하는지
# G층에 갈 수 없다면 use the stairs

# 1<= sg<=f<= 1000000
# F  S  G U D
# 10 1 10 2 1
# 3 5 7 9 11 10
# 0 1 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0 0 0


# 큐에 넣고 뺸값 + U === G
# 큐에 넣고 뺸값 + D === G
# 큐에 넣고 뺸값 0<=: use the stairs
# 큐에 넣고 뺸값 G보다 작으면 append cnt +=1 큐에 넣기
# 큐에 넣고 뺸값 G보다 클 떄 -D가 G이면 cnt 출력 아니면 use the stairs

import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

visited = [0] * (f+1)

def bfs():
    q = deque()
    q.append(s)

    visited[s] = 1

    while q:
        ni = q.popleft()

        if ni == g:
            return visited[ni] - 1

        niu = ni + u
        nid = ni - d

        if 0< niu <= f and visited[niu] == 0:
            visited[niu] = visited[ni] + 1
            q.append(niu)
        if 0< nid <= f and not visited[nid]:
            visited[nid] = visited[ni] + 1
            q.append(nid)
    return "use the stairs"

print(bfs())