def solution(citations):
    answer = 0
    citations.sort(reverse=True) # 내립
    
    for i in range(len(citations)): 
        # H_index가 존재하고 H_index를 넘는 논문이 몇 개인지 구할때
        if(citations[i] <= i):
            # 정렬한 순서보다 값이 작거나 같을 때
            return i

    return len(citations)   # 인용횟수가 모두 동일할 때

# def solution(citations):
#     answer = []
#     for i in range(len(citations)):
#         cnt =0
#         temp = [] # h번 이상 안된 인용된 논문
#         for j in range(len(citations)):
#             if citations[j] >= citations[i]:
#                 cnt+=1
#             else:
#                 temp.append(citations[i])
#         final_chk = 0
#         if cnt >= citations[i]:
#             for k in temp:
#                 if k <=citations[i]:
#                     final_chk+=1
#         if final_chk == len(temp):
#             answer.append(citations[i])
#     return max(answer)

# # 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
# # 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

# # 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations