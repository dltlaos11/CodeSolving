import sys
input = sys.stdin.readline

bracket = input().rstrip()
stack = []
res = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if bracket[i-1] == "(":
            res += tmp
        stack.pop()
        tmp //= 2

# 꺼낸 괄호가 닫는 괄호일 떄, 그 괄호의 직전의 괄호와 쌍이 맞는 경우에만 곱한다(res에 더하기 수행)
    else:
        if not stack or stack[-1] == "(":
            res = 0
            break
        if bracket[i-1] == "[":
            res += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(res)

