def solution(number, k):

    stack = []
    
    for num in number:
        # stack에 마지막 값이 현재 num보다 크면 pass 작으면 pop
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)
    
    # k가 남아있는 경우
    if k != 0:
        stack = stack[:len(number)-k]
    
    return ''.join(stack)

# from itertools import combinations
# from itertools import permutations
# def solution(number, k):
#     answer = 0
    
#     number = list(number)[:len(number)-k]
#     print(number)
    
#     # number = sorted(list(number), reverse=True)[:len(number)-k]
#     # print(number)
    
#     # for num in list(combinations(number,len(number)-k)):
#         # answer = max(, answer)
#         # print(int("".join(num)))
#         # print(typeof("".join(num)))
#     # print(list(permutations(number,k)))
#     return str(answer)