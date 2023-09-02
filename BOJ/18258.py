# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
# push X: 정수 X를 큐에 넣는다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력, 큐에 정수 없다면 -1 출력
# size: 개수
# empty: 스택이 비어있으면 1, 아니면 0 출력
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())
queue = deque()
for t in range(TC):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if len(queue): print(queue.popleft())
        else: print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue): print(0)
        else: print(1)
    elif cmd[0] == "front":
        if len(queue): print(queue[0])
        else: print(-1)
    elif cmd[0] == "back":
        if len(queue):
            print(queue[-1])
        else: print(-1)
# head:int = 0
# head+=1