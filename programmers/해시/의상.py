def solution(clothes):
    answer = 1
    clodict = {}
    for i in clothes:
        clodict[i[1]]=0
    for k in clothes:
        clodict[k[1]]+=1
        # clodict[k[1]]+=len(k[:1])
    for h in clodict.values():
        answer *= (h+1)
    return answer - 1 # 아무것도 안입을 경우