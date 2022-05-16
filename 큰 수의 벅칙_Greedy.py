# 배열의 크기 N, 숫자가 더해지는 횟수 M, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서
# K번을 초과하여 더해질 수 없다. 큰 수의 법칙에 따른 결과를 출력

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = m // (k+1)
count1 = m % (k+1)

res1 = k*first+second
result = count*res1 + count1*first

print(result)