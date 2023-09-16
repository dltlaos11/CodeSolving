import math
import sys
input = sys.stdin.readline

def is_prime1(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i ==0:
            return False
    return True
N, M = map(int, input().split())
for i in range(N,M+1):
    if is_prime1(i) == True:
        print(i)

