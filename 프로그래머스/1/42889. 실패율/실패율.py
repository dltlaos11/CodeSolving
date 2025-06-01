def solution(N, stages):
    answer = []
    fail = []
    counter = 0
    
    for n in range(1, N + 1):
        cnt = 0
        for stage in stages:
            if stage == n:
                cnt += 1
        
        counter += cnt
        if n == 1:
            fail.append({'stage': n, 'fail_p': cnt / len(stages), 'cnt_s': counter})
        else:
            remaining_players = len(stages) - fail[n - 2]['cnt_s']
            fail_rate = cnt / remaining_players if remaining_players > 0 else 0
            fail.append({'stage': n, 'fail_p': fail_rate, 'cnt_s': counter})

    fail.sort(key=lambda x: x['fail_p'], reverse=True)
    
    for n in range(N):
        answer.append(fail[n]['stage'])
    
    return answer
