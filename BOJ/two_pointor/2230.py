# N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]
# 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다),
# 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램
# 첫째 줄에 M 이상이면서 가장 작은 차이를 출력
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

a = [int(input()) for _ in range(n)]
a.sort()

left = 0
right = 0

res =  int(2e9)
# res =  sys.maxsize

while left <= right and right < n:
    if a[right] - a[left] < m:
        right += 1
    else:
        res = min(res, a[right] - a[left])
        left +=1

print(res)
# 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때, 2개의 점의 위치를 기록하면서 처리하는 알고리즘을 의미한다.
# ‘특정한 합을 가지는 부분 연속 수열 찾기’ 또는 ‘정렬되어 있는 두 리스트의 합집합’