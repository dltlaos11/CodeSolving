# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
import sys

input = sys.stdin.readline

TC = int(input())
stack = []
for _ in range(TC):
    cmd = int(input())
    if cmd == 0:
        if stack:
            stack.pop()
    else: stack.append(cmd)

print(sum(stack))
# k: int = int(input().rstrip()) 타입 지정 가능 3.5이상 부터
# stack.pop() if num==0 else stack.append(num) 3항 연산자 구현 가능
