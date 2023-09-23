import sys

input = sys.stdin.readline

n = int(input())
u = [int(input()) for _ in range (n)]

u.sort()
check = True
res = 0
while check:
    max_num = u.pop() # (k)큰 수부터 추출

    for i in range(len(u)):
        left = i
        right = len(u)-1

        while left <= right:
            sum = u[i]+u[left]+u[right]
            if sum<max_num:
                left+=1
            elif sum>max_num:
                right-=1
            else:
                res = max_num
                check = False
                break

print(res)