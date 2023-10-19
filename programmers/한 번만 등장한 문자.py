from collections import Counter


def solution(s):
    res = []
    for i, j in Counter(s).items():
        if j == 1:
            res.append(i)
    return "".join(sorted(res))
    # from collections import Counter
    # Counster(문자열).items()

    # answer = ''
    # ns = sorted(list(set(s)))
    # for i in ns:
    #     if s.count(i) == 1:
    #         answer += i
    # return answer
    # 문자열.count(문자)

    # return "".join(sorted(([c for c in s if s.count(c) == 1])))