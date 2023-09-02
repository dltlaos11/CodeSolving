import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    stack = []
    check = True

    for char in s:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                check = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                check = False
                break

    if s == ".":
        break
    print("yes" if check and not stack else "no")

# 모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝
# 모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝
# 모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재
# 모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
# 짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
# 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단
# 입력의 종료조건으로 맨 마지막에 온점 하나(".")
# 문자열 == 균형 ? yes: no