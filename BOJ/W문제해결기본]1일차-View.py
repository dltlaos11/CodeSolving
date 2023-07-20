T = 10
for i in range(1, T+1):
  N = int(input())
  buildings = list(map(int, input().split()))
  res = 0
  for j in range(2, N-2):
    if(buildings[j]>buildings[j-2] and buildings[j]>buildings[j+2] and buildings[j]>buildings[j-1] and buildings[j]>buildings[j+1]):
      res += buildings[j]-max(buildings[j-2],buildings[j+2],buildings[j-1],buildings[j+1])
  print('#%d %d'%(i,res))

# 원하는 인덱스에 값 수정해서 넣기
# a = [1,2,3,4]
# a[1:4] = [9,9,9]  -> 1 9 9 9

# 원하는 숫자로 배열 채우기
# a = [1 for i in range(100)]
# a = [1] * 100]
# 1206 [S/W 문제해결 기본] 1일차 - View