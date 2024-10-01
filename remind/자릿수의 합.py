temp = {}

def digit_sum(x):
    global temp

    splited = ','.join(x)
    # 숫자만 선별하기
    numbers_only = [int(item) for item in splited if item.isdigit()]
    # isinstance
    try:
        temp[x] = sum(numbers_only)
    except KeyError:
        temp[x] = 0

    return ','.join(x)

n = int(input())

numbers = map(str, input().split())

for i in numbers:
    digit_sum(i)

print(max(temp, key=temp.get))
# 파이썬의 dict 객체는 iterable하기 때문에 max, min, sum 등의 함수와 함께 사용할 수 있습니다. 예를 들어,
# max(temp, key=temp.get)는 딕셔너리 temp의 키를 반복하면서 각 키에 대해 temp.get(key)를 호출