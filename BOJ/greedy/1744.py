import sys
input = sys.stdin.readline

n = int(input())

minus_list = []
plus_list = []
one_list = [] # 1은 더하는게 이득
ans = 0

# 입력값 받기
for i in range(n):
  num = int(input())
  if num > 1:
    plus_list.append(num)
  elif num <= 0:
    minus_list.append(num)
  else:
    one_list.append(num)

plus_list.sort(reverse=True)
minus_list.sort()

# 양수 계산
# 양수의 개수가 홀수라면 제일 작은 값을 정답에 더하기
if len(plus_list) %2 == 1:
  ans += plus_list[len(plus_list)-1]
  for j in range(0, len(plus_list)-1, 2):
    ans += plus_list[j] * plus_list[j+1]
# 양수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
   for j in range(0, len(plus_list), 2):
    ans += plus_list[j] * plus_list[j+1]

# 음수 계산(0 포함)
# 음수의 개수가 홀수라면 제일 큰 값을 정답에 더하기
if len(minus_list) %2 == 1:
  ans += minus_list[len(minus_list)-1]
  for j in range(0, len(minus_list)-1, 2):
    ans += (minus_list[j]) * (minus_list[j+1])
# 음수의 개수가 짝수면 두 수를 곱하고 정답에 더하기
else:
  for j in range(0, len(minus_list), 2):
    ans += (minus_list[j]) * (minus_list[j+1])

for j in range(len(one_list)):
  ans += one_list[j]

print(ans)


# n = int(input())
# arr = [int(input()) for _ in range(n)]
#
# res = sorted(arr)
#
# sum = 0
#
# if len(res) == 1:
#     print(res[0])
#     exit(0)
#
# if len(res)%2 == 0:
#     for i in range(0, len(res), 2):
#         # print(i)
#         if res[i]*res[i+1] > res[i] + res[i+1]:
#             sum += res[i]*res[i+1]
#         else:
#             sum += res[i] + res[i+1]
#     print(sum)
#     exit(0)
#
# if len(res) % 2 == 1:
#     for i in range(len(res)-1, -1, -2):
#         if i == 0:
#             sum += res[i]
#         elif res[i]*res[i-1] > res[i]+res[i-1]:
#             sum += res[i] * res[i-1]
#         else:
#             sum += res[i]+res[i-1]
#     print(sum)
#     exit(0)


        # if res[]
    #     if res[i] * res[i + 1] > res[i] + res[i + 1]:
    #         sum += res[i] * res[i + 1]
    #     else:
    #         sum += res[i] + res[i + 1]
    # print(sum)
# print(sum)

# 4
# -1 2 1 3
# -1 + 2*3 + 1
# -1 1 2 3
# 0

# 곱하기
# 큰수끼리 곱하기
#

# 더하기
# sort
# i*(i+1) > i + i+1
# sum += i + i+1

# 6
# 0 1 2 4 3 5
# 0 + 5*4 + 3*2 +1

# 1
# -1

# 3
# -1 0 1
# -1*0 + 1

# 2
# 1 1
# 1 + 1 -> 곱하기 더하기 비교

# 5
# 1 2 3 4 5
# 3 12 5
# 20 6 1

# -3 2 3 4 5
# -1 12 5
# 20 6 -3

# -3 -2 -1 1 1 1 2
# 5
# -1