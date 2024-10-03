from math import sqrt

temp = []

def reverse(x):
    # 첫 자리 0이면 무시
    # reversed_s = x[::-1]
    # reversed_s = ''.join(reversed(str(x)))
    # ignore_zero = [item for item in reversed_s if item != '0']

    res = 0

    while x > 0:
        t = x % 10
        res = res * 10 + t
        x=x//10

    return res

def isPrime(x):

    # if int(x) ==1:
    #     return False
    # for i in range(2, int(sqrt(int(x))) + 1):
    #     if int(x) % i ==0:
    #         return False
    # else:
    #     return True

    global temp

    is_prime = [True] * (int(x) + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(int(x))) + 1):

        if not is_prime[i]:
            continue

        for j in range(2*i, int(x)+1, i):
            is_prime[j] = False

    if is_prime[int(x)]:
        temp.append(int(x))

    return is_prime[int(x)]

n = int(input())

numbers = list(map(int, input().split()))

for i in numbers:
    # tmp = reverse(i)
    # if isPrime(tmp):
    #     print(tmp, end=' ')

    isPrime(reverse(i))
print(*temp)