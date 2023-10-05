n, m = map(int, input().split())
arr = []


def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        arr.append(i)
        dfs()
        arr.pop()
        #  arr : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
dfs()