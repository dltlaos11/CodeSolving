N, M = map(int, input().split())
cnt = 0
while N >= M:
    while N % M != 0:
        N -= 1
        cnt += 1
    N //= M
    cnt += 1
while N >1:
    N -=1
    cnt+=1
print(cnt)

# N이 M의 배수가 될 떄까지 1씩 뺴기
# N을 M으로 나누기
# 1이 될 떄까지 최소의 횟수를 구하는 문제