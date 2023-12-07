from itertools import permutations
def solution(k, dungeons):
    charge = k
    temp =[]
    for hardness in list(permutations(dungeons)):
        cnt = 0
        for hard in hardness:
            if k >= hard[0]:
                k -= hard[1]
                cnt +=1
            else:
                k = charge
                break
        temp.append(cnt)
    answer =max(temp)
    return answer