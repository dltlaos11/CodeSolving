def solution(food):
    answer = ''
    half = ''
    
    for i in range(len(food)):
        tmp = ''
    
        # 없으면 몫
        if food[i] % 2 == 0:
            tmp += str(i)
            half += tmp * (food[i]//2)
            
        # 나머지 있으면 몫 * 나머지
        else:
            # continue
            tmp += str(i)
            half += str(i) * (food[i] // 2)
            
    half2 = half[::-1]
    
    answer += half + '0' + half2
    
    return answer