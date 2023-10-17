import copy


# 슬라이싱[start:stop:step]
# a = [1,2,3,4,5,6,7,8,9]
# a[::2] => 1 3 5 7 9
# a[1::2] => 2 4 6 8

arr = [1,2,3,5,[1,2]]
a = arr # 얕은 복사
# a = arr[:] 완전한 깊은 복사도 아니고, 완전한 얕은 복사도 아님. 그렇지만 이것 또한 얕은 복사로 구분
# a = copy.copy(arr)

a = copy.deepcopy(arr) # 깊은 복사
arr[0] = 99

print(a)
print(id(a) == id(arr))

def solution(my_string):
    # answer = []
    # for i in range(len(my_string)-1, -1, -1):
    #     answer.append(my_string[i])
    # return "".join(answer)

    return my_string[::-1]