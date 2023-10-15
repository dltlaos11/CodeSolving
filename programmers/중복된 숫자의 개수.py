def solution(array, n):
    return len(list(filter(lambda x: x == n, array)))
def solution(array, n):
    return array.count(n)
# [1, 1, 2, 3, 4, 5, 11] -> 전체 1의 개수

from collections import Counter
def solution(array, n):
    answer = Counter(array).get(n)
    return 0 if answer == None  else answer
# 파이썬은 null대신 None