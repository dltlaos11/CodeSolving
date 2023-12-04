def solution(brown, yellow):
    answer = []
    total = brown + yellow                  # a * b = total

    # a >= b, 긴 쪽먼저 탐색
    for a in range(total+1, 0,-1): 
        b = total / a
        if 2*a + 2*b -4 == brown:  # 2*a + 2*b -4 = brown
            return [a,b]
         
    return answer

# a: 가, b:세
# a >= b
# 2a + 2b -4 = brown
# (a-2) * (b-2) = yellow
# brown + yellow = ab