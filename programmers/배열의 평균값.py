def solution(numbers):
    answer = 0
    for i in (numbers):
        answer += i
    return answer/len(numbers)

def solution(numbers):
    return sum(numbers)/len(numbers)

# 다차원 배열에서의 sum이 가능
import numpy as np
def solution(numbers):
    return np.sum(numbers)/len(numbers)
# print(np.sum([[0,1], [0, 5]])) 6
# print(np.sum([[0,1], [0, 5], [0,6]], axis=1)) [1 5 6] 1차원
# print(np.sum([[0,1], [0, 5]], axis=0)) [0, 6] 2차원
