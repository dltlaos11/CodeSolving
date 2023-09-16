import math
import sys
input = sys.stdin.readline

def is_prime1(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i ==0:
            return False
    return True
N = int(input())
s = (input().rstrip().split())
res = []
for i in s:
    if is_prime1(int(i)) == True:
        res.append(i)
print(len(res))


# 소수판별
# def is_prime(x):
#     if x == 1: return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
