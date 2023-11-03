from itertools import combinations

def solution(nums):
    cnt = 0

    for i in list(combinations(nums, 3)):
        # (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)
        flag = True
        for j in range(2, sum(i)):
            if sum(i) % j == 0:  # 소수라면
                flag = False
                break
        if flag:
            cnt += 1

    return cnt

# print(list(combinations(nums, 2)))
# # 자기 자신 및 다른 요소와 중복되지 않은 조합 튜플
# print("-------------------------")
# print(list(combinations_with_replacement(nums, 2)))
# # 자기 자신 및 다른 요소와 중복 조합 튜플
# print("-------------------------")
# print(list(permutations(nums, 2)))
# # 자기 자신을 포함하지 않는 순열
# print("-------------------------")
# print(list(product(nums, repeat=2)))
# # 자기 자신을 포함 순열 -> 모든 경우의 수
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# -------------------------
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
# -------------------------
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
# -------------------------
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3),
#  (4, 4)]