from collections import deque
def solution(priorities, location):
    answer = 1
    q=deque(priorities)
    
    while len(q)>1:
        tmp=q.popleft()
        if tmp<max(q):
            q.append(tmp)
            if location==0:
                location=len(q)-1
            else:
                location-=1
        else:
            if location==0:
                return answer # 첫번째
            else:
                answer+=1
                location-=1
                
    return answer