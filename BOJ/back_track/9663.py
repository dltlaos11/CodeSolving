import sys
input = sys.stdin.readline

n = int(input())

ans = 0
row = [0] * n


def search_loc(x): # 퀸을 놓지 못하는 경우
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if search_loc(x):
                n_queens(x + 1)

n_queens(0)
print(ans)