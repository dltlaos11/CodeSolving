import re


def solution(order):
    answer = 0
    # for i in str(order):
    #     if i in ('3', '6', '9'):
    #         answer +=1
    # return answer

    order = str(order)
    # answer += order.count('3') count, 성공 시 1 반환
    # answer += order.count('6')
    # answer += order.count('9')
    # return answer

    # return sum(map(lambda x: order.count(x), '369')) 람다

    # return len(list(filter(lambda x: x in '369', order)))

    # return len(re.findall('[369]', order)) 정규표현식