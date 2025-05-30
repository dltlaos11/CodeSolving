def solution(name, yearning, photo):
    answer = []
    
    type = {}
    
    for idx in range(len(name)):
        type[name[idx]] = yearning[idx]
    
    for fir in photo:
        print(fir)
        tmp = 0
        for sec in fir:
            if sec in name:
                tmp += type[str(sec)]
        answer.append(tmp)
    
    return answer