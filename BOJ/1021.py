import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
loc = list(map(int, input().split()))
queue = deque([i for i in range(1, N+1)])

cnt = 0
for i in loc:
    while queue:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1
print(cnt)
# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

# 2,3번 연산일 떄만 +1
# 최소 최대 구분
# 왼쪽에 가까우면 2번
# 오른쪽에 가까우면 3번

# index
# [2,2] -> 첫번쨰 idx 값