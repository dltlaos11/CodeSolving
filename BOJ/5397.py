import sys

input = sys.stdin.readline

TC = int(input())
for i in range(TC):
    cmd = input().rstrip()
    lStack = [];
    rStack = [];
    for j in cmd:
        if j == '<':
            if lStack: rStack.append(lStack.pop())
        elif j == '>':
            if rStack: lStack.append(rStack.pop())
        elif j == '-':
            if lStack: lStack.pop()
        else: lStack.append(j)
    # print(lStack, reversed(rStack), ''.join(lStack.extend(reversed(rStack))))
    print("".join(lStack) + "".join(rStack[::-1]))
# 리스트를 합치는 다양한 방법
# ret = a + b
# a.append(b)
# b의 원소가 그대로 하나의 값으로 추가 됨
# a = [1, 2, 3], b = [[4, 5]] -> a = [1, 2, 3, [4, 5]]
# a = [1, 2, 3], b = ['hi'] -> a = [1, 2, 3, 'hi]
# a.extend(b)
# iterable 요소 하나하나가 개별로 추가
# a = [1, 2, 3], b = [[4,5]] -> a = [1, 2, 3, 4, 5]
# b = [1, 2, 3], b = ['hi'] -> a = [1, 2, 3, 'h', 'i']