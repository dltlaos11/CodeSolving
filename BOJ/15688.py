import sys
input = sys.stdin.readline

TC = int(input())
arr = []
for _ in range(TC):
    N = int(input())
    arr.append(N)
for i in sorted(arr):
    print(i)

# 임의의 배열에 음수 고려
# import sys
#
# input = sys.stdin.readline
# print = sys.stdout.write
#
# n: int = int(input())
# maxSzie = 1_000_000
#
# numbers = [0 for _ in range((maxSzie * 2) + 1)]
#
# for i in range(n):
#     numbers[int(input()) + maxSzie] += 1
#
# for i in range(maxSzie * 2 + 1):
#     for j in range(numbers[i]):
#         print("{}\n".format(i - maxSzie))
