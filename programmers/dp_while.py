def solution(a):
    answer = a

    dp = [0] * 100
    n = 1
    c = 1
    while a != 0:
        c += 1
        n += 1
        if n % 3 == 0:
            n += 1
        while True:
            if 3 in [int(char) for char in str(n)]:
                n += 1
                if n % 3 == 0:
                    n += 1
            else:
                break
        dp[c] = n
        a -= 1

    return dp[answer]
    # answer = 0
    # for _ in range(n):
    #     answer +=1
    #     while '3' in str(answer) or answer % 3 ==0:
    #         answer +=1
    # return answer

    # dp
    # return [i for i in range(1, 1001) if i % 3!=0 and not('3' in str(i))][n-1]