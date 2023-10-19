# def solution(array, n):
#     array = sorted(array)
#     min = float('inf') 두수간의 차
#     res = 0 위치

#     for i in array:
#         if abs(n-i) < min:
#             min = n - i
#             res = i
#     return res

def solution(array, n):
    return sorted(array, key=lambda x: (abs(n - x), x - n))[0]  # x-n 정렬 기준