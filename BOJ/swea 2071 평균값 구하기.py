N = int(input())
def avg(list):
    sum = 0
    for i in range(10):
        sum += list[i]
    return sum/10
for i in range(1,N+1):
    data = list(map(int, input().split()))
    print('#%d %d' % (i, round(avg(data))))


# 함수를 안쓰고 풀 수 있었지만 뭔가 함수 사용에 익숙해지고 싶어서 함수를 사용하여 풀어보았다.
# 반올림 할 때는 round() 함수 사용 !

# 이렇게 만들 수도 있다.
# def avg(list):
#     return (sum(list)/len(list))
# data = list(map(int, input().split()))
# print(avg(data))