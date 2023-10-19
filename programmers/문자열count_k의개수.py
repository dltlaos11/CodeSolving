def solution(i, j, k):
    answer = 0
#   counst -> 문자열만
#   list(range(1,3)) -> 1, 2
    return str(list(range(i, j+1))).count(str(k))