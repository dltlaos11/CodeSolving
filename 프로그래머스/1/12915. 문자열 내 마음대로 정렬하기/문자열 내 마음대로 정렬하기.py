def solution(strings, n):
    answer = []
    comArr = []
    strings.sort()

    # 추출
    for string in strings:
        comArr.append(string[n])
        
    # 정렬
    findSameIdx = sorted(comArr) # ['c', 'c', 'x']
    print(findSameIdx)
    
    ## 같은 경우 예외처리
    
    for idx in findSameIdx:
        for string in strings:
            if idx == string[n] and string not in answer:
                answer.append(string)
                print(answer)
    
    
    return answer