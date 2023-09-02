# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())
queue = deque()
for _ in range(TC):
    cmd = input().split()
    if cmd[0] == "push_front":
        queue.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        queue.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(queue): print(queue.popleft())
        else: print(-1)
    elif cmd[0] == "pop_back":
        if len(queue): print(queue.pop())
        else: print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if len(queue) == 0: print(1)
        else: print(0)
    elif cmd[0] == "front":
        if len(queue): print(queue[0])
        else: print(-1)
    elif cmd[0] == "back":
        if len(queue): print(queue[-1])
        else: print(-1)
