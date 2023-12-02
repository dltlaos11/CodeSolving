def solution(numbers, target):
    leaves = [0]  # 모든 계산 결과를 담자, 끝입니다.. 네, 
    # 완벽이진트리 재방문할 필요 없다.[+num] [-num]
    count = 0
    
    for num in numbers:
        
        temp = []
        
        for leaf in leaves:
            temp.append( leaf + num)
            temp.append( leaf - num)
        
        leaves = temp
    
    for leaf in leaves:
        if leaf == target:
            count +=1
            
    return count