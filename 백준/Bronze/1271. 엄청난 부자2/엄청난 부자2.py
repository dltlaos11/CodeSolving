numbers = list(map(int, input().split()))

# 첫 번째 숫자와 두 번째 숫자를 선택
num1 = numbers[0]
num2 = numbers[1]

# 몫과 나머지 계산
quotient = num1 // num2
remainder = num1 % num2

print(quotient)
print(remainder)