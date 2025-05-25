from math import sqrt


def get_divisors(n):
    s = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    return s

def solution(number, limit, power):
    answer = 0
    divisor_list = []
    
    for i in range(1, number+1):
        divisor_list.append(len(get_divisors(i)))

    for i in divisor_list:
        if i > limit:
            answer += power
        else:
            answer += i
            
    return answer