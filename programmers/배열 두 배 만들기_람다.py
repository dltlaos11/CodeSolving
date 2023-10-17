import numpy as np


def solution(numbers):
    # answer = []
    # for i in numbers:
    #     answer.append(i*2)

    # return list(map(함수, 이터러블 객체))
    # return list(map(lambda x: x*2, numbers))
    numbers = np.array(numbers)
    return (numbers * 2).tolist()