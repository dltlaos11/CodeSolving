def solution(n, lost, reserve):
    answer = n
    spare_stolen = set(lost) & set(reserve)
    # reserve, lost 한 자식..
    lost = sorted(list(filter(lambda x : x  not in spare_stolen, lost)))
    reserve = sorted(list(filter(lambda x : x not in spare_stolen, reserve)))

    for i in lost:
        if i-1 in reserve:
            # reserve.pop(reserve.index(i-1))
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            n -=1
    
    return n
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어,
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.

# 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve
# 체육수업을 들을 수 있는 학생의 최댓값을 return