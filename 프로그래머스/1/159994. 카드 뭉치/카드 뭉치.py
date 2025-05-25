from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    for i in range(len(goal)):
        chk = goal.popleft()
        
        if chk in cards1:
            if cards1.popleft() == chk:
                continue
            else:
                answer = 'No'
        
        if chk in cards2:
            if cards2.popleft() == chk:
                continue
            else:
                answer = 'No'
        
#     1배열 체크 2배열 체크해서
#     goal popleft해서 배길이 0이면 yes
    
    return answer