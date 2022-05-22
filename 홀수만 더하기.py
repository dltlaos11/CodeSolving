t = int(input())

for i in range(1, t+1):
  data = list(map(int, input().split()))
  result = 0
  for j in data:
    if j%2 == 1:
      result += j
  print('#%d %d' % (i, result))
# 출력 형식
# print('#%d %d' %(i, result))
# '%d %d' %(i, result)
