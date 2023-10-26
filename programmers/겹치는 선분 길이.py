def solution(lines):
#     하나의 배열에 범위 check
#     answer = 0
#     line = [0 for i in range(200)] # -를 고려한 전체 배열 선언
#     for a, b in lines: 
#         while a < b: 
#             line[a+100] += 1 # 전체 배열에 1을 더해 배열 check
#             a+=1
            
#     return len(list(filter(lambda x: x>1, line)))

    # 집합사용으로 풀기
    answer = 0
    a = set(range(lines[0][0], lines[0][1]))
    b = set(range(lines[1][0], lines[1][1]))
    c = set(range(lines[2][0], lines[2][1]))
    
    return len(a&b | b&c |c&a)
