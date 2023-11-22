def solution(arr):
    
    answer = []
    arr.append('x')
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    return answer

    # ans=[]
    # for i in range(0,len(arr)-1):
    #     if arr[i] != arr[i+1]:
    #         ans.append(arr[i])
    # print(ans)
    # ans.append(arr.pop())
    # return ans