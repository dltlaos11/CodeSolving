T = int(input())
for test_case in range(1, T + 1):
    square_len, dead_pari = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(square_len)]


    res = []
    for i in range(square_len):
        for j in range(square_len):
            if j <= square_len-dead_pari and i <= square_len-dead_pari:
                temp = []
                for z in range(1,dead_pari+1):
                    for k in range(1,dead_pari+1):
                        temp.append(graph[i+dead_pari-z][j+dead_pari-k])
                res.append(sum(temp))

    print(f'#{test_case} {max(res)}')