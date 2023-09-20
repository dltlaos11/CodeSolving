# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램
# 이진탐색은 요소들이 정렬된 리스트
# 이진탐색은 검색범위를 조절할때, 현재 값보다 뒤에 있는 값은 현재 값보다 크고, 앞에 있는 값은 현재 값보다 작다는 것을 전제
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))

m = int(input())
a2 = list(map(int, input().split()))

def binary_search(target, data):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True

        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


for i in a2:
    if binary_search(i, a):
        print(1)
    else:
        print(0)