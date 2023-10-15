def solution(n):
    answer = 0
    cnt = n // 2
    for i in range(1, cnt + 1):
        answer += i * 2

    return answer
def solution(n):
    return sum(range(0, n+1, 2))