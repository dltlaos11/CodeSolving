T = int(input())

for test_case in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]

    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    res = 1

    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(graph[i][j])
            col.append(graph[j][i])
        if set(row) != check:
            res = 0
        if set(col) != check:
            res = 0

    for k in range(3, 10, 3):
        for q in range(3):
            temp = []
            for i in range(k - 3, k):
                for j in range(3 * q, 3 * q + 3):
                    temp.append(graph[i][j])
            if set(temp) != check:
                res = 0
    print(f"#{test_case} {res}")