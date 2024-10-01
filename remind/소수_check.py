from math import sqrt

n = int(input())

is_prime = [True] * (n + 1)  # 처음에는 모두 true로 초기화
is_prime[0] = False  # sum
is_prime[1] = False  # 1은 소수가 아니므로

# 에라토스테네스의 체 알고리즘
# 2 to 루트n
for i in range(2, int(sqrt(n)) + 1):

    if not is_prime[i]:
    	continue

    for j in range(2 * i, n + 1, i):
        is_prime[j] = False

print(sum(is_prime))

# temp = []
#
# for i in range(1, n+1):
#     cnt = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             cnt += 1
#     if cnt == 2:
#         temp.append(i)
#
# print(temp)
