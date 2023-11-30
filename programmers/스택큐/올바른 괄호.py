def solution(s):
    answer = True
    
    res = 0
    
    for i in s:
        if i == "(":
            res +=1
        if i == ")":
            res -=1
        if res<0:
            return False
    
    if res != 0:
        return False

    return True

# 순차적으로 검사
# res 비교 -> cnt
