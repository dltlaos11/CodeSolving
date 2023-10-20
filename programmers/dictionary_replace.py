def solution(numbers):
    answer = ''
    num = {}
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    for i in range(len(arr)):
        num[arr[i]] = i

    temp = ''
    for i in numbers:
        temp += i
        if temp in list(num.keys()):
            answer += str(num[temp])
            temp = ''

    # numbers.replace('one', 1).replace('two',2)...

    return int(answer)