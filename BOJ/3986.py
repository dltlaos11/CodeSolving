import sys

input = sys.stdin.readline

TC = int(input())
cnt = 0
for i in range(TC):
    s = input().rstrip()
    stack = []
    for char in range(len(s)):
        if stack and stack[-1] == s[char]:
            stack.pop()
        else: stack.append(s[char])
    if not stack: cnt +=1
print(cnt)