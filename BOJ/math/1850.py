import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

def gcd(a,b):
    if(a == 0): return b
    return gcd(b%a, a)

for _ in range(gcd(a,b)):
    print("1", end="")

# 유클리드 호제법

# 두수 A,B에 대해 A를 B로 나눈 나머지를 r이라고 하면 GCD(A,B) =GCD(B,r)
# GCD(20,12) = GCD(12, 8) = GCD(8,4) = GCD(4,0) = 4