def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            # sorted['z', 'd', 'x'] == sorted['dzx']
            # {'d', 'z', 'x'} == {'z', 'x', 'd'}
            return 1

    return 2

from collections import deque

def solution(A, B):
    answer = 0
    a = deque(A)
    for i in range(len(A)):
        if list(a) == list(B):
            return answer
        a.appendleft(a.pop())
        answer += 1

    return -1

    # return (B*2).find(A)

def solution(emergency):
    return list(map(lambda x: sorted(emergency, reverse=True).index(x)+1, emergency))
# [3, 76, 24] -> [3, 1, 2]
# [1, 2, 3, 4, 5, 6, 7] -> [7, 6, 5, 4, 3, 2, 1]