from itertools import permutations
def solution(k, dungeons):
    temp = []
    for hardness in list(permutations(dungeons)):
        charge = k
        cnt = 0
        for hard in hardness:
            if charge >= hard[0]:
                charge -= hard[1]
                cnt +=1
            else:
                break
        temp.append(cnt)
    answer = max(temp)
    return answer