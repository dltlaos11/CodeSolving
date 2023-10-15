def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer +=1
    return answer

def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

def solution(array, height):
    array.append(height)
    return sorted(array, reverse=True).index(height)

def solution(array, height):
    # print(filter(lambda x: x > height, array)) 	<filter object at 0x7f25703d9550>
    # print(list(filter(lambda x: x > height, array))) 〉	[180, 192, 170]
    return len(list(filter(lambda x: x> height, array)))