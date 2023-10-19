# def fac(x):
#     res = 1
#     for i in range(1, x+1):
#         res = res * i
#     return res

# def solution(n):
#     answer = 0
#     x = 1
#     while True:
#         if fac(x) > n:
#             return x-1
#         else:
#             x+=1

# 2
# def solution(n):
#     fac = 1
#     i = 1
#     while fac <= n:
#         i += 1
#         fac *= i
#     return i - 1

from math import factorial
def solution(n):
    i = 1
    while factorial(i) <= n:
        i += 1
    return i-1