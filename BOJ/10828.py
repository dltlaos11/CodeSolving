# 정수를 저장하는 스택을 구현 -> 입력으로 주어지는 명령을 처리하는 프로그램
# push X: 정수 X를 스택에 넣는다
# pop: 가장위에 있는 정수를 뺴고, 그 수를 출력. 만약 스택에 정수가 없다면 -1출력
# size: 스택에 들어있는 개수 출력
# empty: 스택이 비어있으면 1, 아니면 0 출력
# top: 스택의 가장 위에있는 정수 출력. 만약 스택에 들어있는 정수가 없는 경우 -1출력
import sys

input = sys.stdin.readline

TC = int(input())
stack = []
for t in range(TC):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[-1])
    elif cmd[0] == "pop":
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif cmd[0] == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    else: print(len(stack))