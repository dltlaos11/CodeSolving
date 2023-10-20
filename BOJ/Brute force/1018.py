n, m = map(int, input().split())

result = []
board = [input() for _ in range(n)]
# 부르트포스
# 8*8의 크기로 잘라서 가로,세로 모두 검사
for i in range(n - 7):
    for j in range(m - 7):
        # 시작점이 바뀔 때마다 처음부터 칠하기 위해 draw 변수 선언
        # 시작 지점이 검은색, 흰색일 경우를 대비해 2개의 변수 선언
        draw1 = 0 # W로 시작하는 경우 바뀌어야 할 체스판의 개수
        draw2 = 0 # B로 시작하는 경우 바뀌어야 할 체스판의 개수
        # 시작점부터 8x8 크기의 체스판을 탐색
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                # board[a][b]지점이 2로 나눈 나머지가 0일때 1일떄를 기준으로 어느 색을 칠할지 결정
                # (i + j) % 2 == 0일 경우 'W'
                # (i + j) % 2 != 0일 경우 'B'
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1

                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1
        # 8x8 크기의 체스판을 모두 칠했을 경우 결과 리스트에 추가
        # 시작점이 바뀔 떄마다 B색으로 칠한 경우, W색으로 칠한 경우가 리스트에 담김
        result.append(draw1)
        result.append(draw2)

print(min(result))
