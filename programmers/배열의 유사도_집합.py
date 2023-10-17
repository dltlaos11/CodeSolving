print(len(set(["a", "b", "c"]) & set(["a", "b", "dawadwa", "c", "com"]))) # 교집합
print(len(set(["a", "b", "c"]) | set(["a", "b", "dawadwa", "c", "com"]))) # 합집합
def solution(s1, s2):
    cnt = 0
    for i in s1:
        if i in s2:
            cnt +=1
    return cnt
def solution(s1, s2):
    # return len(s1) + len(s2) - len(set(s1 + s2))
    return len(s1) + len(s2) - len(set(s1) |  set(s2))