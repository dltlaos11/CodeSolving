from collections import deque


def solution(numbers, direction):
    answer = []
    if direction == "right":
        # answer = [numbers[-1]] + numbers[:-1]
        q = deque(numbers)
        q.rotate(1)
    else:
        # answer = numbers[1:]+[numbers[0]]
        q = deque(numbers)
        q.rotate(-1)

    # if direction == "right":
    #     q = deque(numbers)
    #     q.appendleft(numbers[-1])
    #     q.pop()
    #     answer = list(q)
    # else:
    #     q = deque(numbers)
    #     q.append(q.popleft())
    #     answer = list(q)

    return list(q)