N = int(input())

for i in range(1, N+1):
    M = int(input())
    data = list(map(int, input().split()))

    data = data[::-1]
    max_value = data[0]
    earn = 0

    for j in range(1, M):
        if(max_value > data[j]):
            earn = earn + (max_value-data[j])
        else:
            max_value = data[j]
    print('#%d %d' %(i, earn))
# N: 전체 케이스 숫자
# M: 각 케이스의 전체 일수를 의미
# 처음 이 문제를 이해하는데 어려움이 있었다.. 예시를 보고 출력결과를 보는데 이해가 되지 않아 한참 해멨다..
# 이 문제의 중요한 Solution은 배열의 뒤에서부터 확인하여 뒤집은 배열의 첫 번째 값을 최대값으로 정한 후 배열의 두 번쨰 값과 비교하며
# 최대값보다 작으면 이득을 본것이니 "이득 : (최대값-다음값)"을 이득(earn)에 더해주고
# 다음값이 최대값보다 크다면 이득을 보지 못한것이니 최대값으로 업데이트해주면 된다.