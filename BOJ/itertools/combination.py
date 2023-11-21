def comb(n, m):
    if n == m or m == 0:
        return 1
    return comb(n - 1, m - 1) + comb(n - 1, m)

def main():
    # nCr, n개중 r개를 뽑는다
    n, m = map(int,(input().split()))
    return comb(n+m,n)
# 8C2 == 8C6
if __name__ == '__main__':
    print(main())

