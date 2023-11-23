def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        if len(arr) >= commands[i][2] - 1:
            answer.append(arr[commands[i][2]-1])
        else:
            answer.append(arr[-1])
    return answer