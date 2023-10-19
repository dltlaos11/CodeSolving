def solution(my_str, n):
#     answer = []

#     x = len(my_str)
#     i =1
#     while x>0:
#         answer.append(my_str[(i-1)*n:i*n])
#         x -= n
#         i +=1
#     return answer

    return [my_str[i:i+n] for i in range(0, len(my_str), n)]