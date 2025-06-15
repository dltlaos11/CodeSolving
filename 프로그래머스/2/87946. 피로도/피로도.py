def solution(k, dungeons):
    answer = []
    R = len(dungeons)
    check = [False for i in range(R)]
    temp = []
    
    def permutation(level):
        
        if level == R:
            
            charge = k
            cnt = 0
            for hard in temp:
                if charge >= hard[0]:
                    charge -= hard[1]
                    cnt +=1
                else:    
                    break
            answer.append(cnt)
            return
        
        for i in range(len(dungeons)):
            
            if check[i] == True:
                continue
            
            check[i] = True
            temp.append(dungeons[i])
            permutation(level+1)
            temp.pop()
            check[i] = False

    permutation(0)
    answer = max(answer)
    
    return answer