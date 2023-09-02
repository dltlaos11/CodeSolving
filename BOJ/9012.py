import sys

input = sys.stdin.readline

TC = int(input())
cnt = 0
for _ in range(TC):
    s = input().rstrip()
    stack = []
    check = True

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                check = False
                break
    print("YES" if check and not stack else "NO")