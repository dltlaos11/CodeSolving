def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i
        if budget >= 0:
            cnt +=1
    return cnt
# 그리디
# 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.
# 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.
# 부서별로 신청한 금액이 들어있는 배열 d, 예산 budget
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return