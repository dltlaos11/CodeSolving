from collections import deque

def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        temp.append(100 - progresses[i])
    
    for i in range(len(speeds)):
        cnt = 0
        while(temp[i] > 0):
            temp[i] -= speeds[i]
            cnt +=1
        answer.append(cnt)
    
    answer = deque(answer)
    temp = []
    result = []
    temp.append(answer.popleft())
    
    while (len(answer) != 0):
        answer_temp = answer.popleft()
        if answer_temp > max(temp):
            result.append(len(temp))
            temp = []
        temp.append(answer_temp)
        
    if len(temp) > 0:
        result.append(len(temp))
    
    return result
