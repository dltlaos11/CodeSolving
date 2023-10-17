def solution(rsp):
    # answer = []
    # answer = ''
    # for i in rsp:
    #     if i == "2":
    #         answer.append("0")
    #         # answer += '0'
    #     elif i == "0":
    #         answer.append("5")
    #     else:
    #         answer.append("2")
    # return "".join(answer)

    ans = {'2': '0', '0': '5', '5': '2'}
    res = ''
    #     2
    # for i in rsp:
    #     res += ans[i]
    # return res

    #     3
    return "".join([ans[i] for i in rsp])