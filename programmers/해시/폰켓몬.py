from itertools import combinations
def solution(nums):
    all_types = len(set(nums)) # 중복 제거한 종류
    min_types = len(nums)//2 # 고를 수 있는 종류
    answer = min(all_types, min_types)
#     answer = 0
#     arr = list(combinations(nums, len(nums)//2))
#     for i in arr:
#         cnt = 0
#         temp = []
#         for j in i:
#             print(i)
#             if j not in temp:
#                 cnt+=1
#             temp.append(j)

#         answer = max(answer, cnt)
    
    return answer