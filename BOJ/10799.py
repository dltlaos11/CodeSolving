# 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다
# 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다
# 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
# 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

# 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현
# 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현

import sys

input = sys.stdin.readline

s = input().rstrip()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append("(")
    else:
        if s[i - 1] == "(":
            stack.pop()
            cnt += len(stack)

        else:
            stack.pop()
            cnt += 1
print(cnt)