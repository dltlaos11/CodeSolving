def solution(participant, completion):
    answer = ''
    check_looser={}
    sum_hash=0
    
    for par in participant:
        check_looser[hash(par)] = par
        sum_hash += hash(par)
    
    for com in completion:
        sum_hash -= hash(com)
    
    return check_looser[sum_hash]