def solution(my_string):
    answer = ''
    return ("".join(dict.fromkeys(my_string))) # 순서있는 set

def solution(before, after):
    # return 1 if sorted(list(before)) == sorted(list(after)) else 0

    af = list(after)
    bf = list(before)
    for i in bf:
        print(i)
        if i in af:
            af.remove(i)  # 리스트 제거 -> pop x remove
        else:
            return 0
    return 1

