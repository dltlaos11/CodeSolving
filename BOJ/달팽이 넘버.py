T = int(input())

# row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for test_case in range(1, T + 1):

    sqr_length = int(input())
    sqr = [[0 for i in range(sqr_length)] for _ in range(sqr_length)]

    # 초기 위치 & 회전방향 설정
    r, c = 0, 0
    dist = 0  # 0:우, 1:하, 2:좌, 3:상

    for i in range(1, sqr_length*sqr_length+1):
        sqr[r][c] = i
        r += dr[dist]
        c += dc[dist]

        # 범위를 벗어나거나 0이 아닌 다른 값이 이미 있다면, dist 방향 체인지
        # 근데 이런 경우라면 요소 인덱스를 다시 원위치시켜줘야하므로 빼줘야함
        # 그런다음 dist의 방향을 바꾸고, 방향 바꿨으면 다시 움직일 수 있도록 행렬 인덱스 업데이트
        if r < 0 or c < 0 or r >= sqr_length or c >= sqr_length or sqr[r][c] != 0:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
            # dist는 % 4 안해주면 0123, 4567, ... 이런식으로 숫자 커지므로 나머지로 접근
            dist = (dist + 1) % 4
            r += dr[dist]
            c += dc[dist]

    print(f'#{test_case}')
    for row in sqr:
        print(*row)

# --------------------------------2
T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(T, T+1):

    snail = int(input())

    graph = [[0] * snail for _ in range(snail)]
    # graph = [[1] * snail for _ in range(snail)]

    dist = 0
    # dist = [0,1,2,3]

    r = 0
    c = 0

    for j in range(1, snail*snail+1):

        graph[r][c] = j
        # graph[dr[dist]+r][dc[dist]+c] = j

        r += dr[dist]
        c += dc[dist]
        # r += dr[dist] + 1
        # c += dc[dist] + 1
        # r += 1
        # c += 1

        if r < 0 or c < 0 or r >= snail or c >= snail or graph[r][c] != 0:
            r -= dr[dist]
            c -= dc[dist]
            # r -= 1
            # c -= 1

            dist = (dist+1) % 4
            # dist += (dist+1) % 4

            r += dr[dist]
            c += dc[dist]

    print(graph)