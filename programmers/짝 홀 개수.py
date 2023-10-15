def solution(num_list):
    even = len(list(filter(lambda x: x % 2 == 0, num_list)))
    odd = len(list(filter(lambda x: x % 2 != 0, num_list)))
    answer = []
    answer.append(even)
    answer.append(odd)
    return answer

def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i % 2 ==0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1
    return answer
