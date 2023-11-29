def solution(answers):
    answer = []
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    fir_scr, sec_scr, thr_scr = 0, 0, 0
    for i in range(len(answers)):
        fir_ptn = i % len(fir)
        sec_ptn = i % len(sec)
        thr_ptn = i % len(thr)
        if fir[fir_ptn] == answers[i]:
            fir_scr += 1
        if sec[sec_ptn] == answers[i]:
            sec_scr += 1
        if thr[thr_ptn] == answers[i]:
            thr_scr += 1
    max_val = max(fir_scr, sec_scr, thr_scr)
    if max_val == fir_scr:
        answer.append(1)
    if max_val == sec_scr:
        answer.append(2)
    if max_val == thr_scr:
        answer.append(3)
            
    return answer

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.