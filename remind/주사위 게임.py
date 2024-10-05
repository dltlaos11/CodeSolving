n = int(input())

temp = []

for i in range(n):
    nums = list(map(int,input().split()))
    cnt_nums = set(nums)
    if len(cnt_nums) == 1:
        temp.append(nums[0]*1000+10000)
    elif len(cnt_nums) == 2:
        cnt = 0
        for j in nums:
            if j == sorted(list(cnt_nums))[0]:
                cnt +=1
        if cnt == 1:
            temp.append(sorted(list(cnt_nums))[1] * 100 + 1000)
        else:
            temp.append(sorted(list(cnt_nums))[0]*100 + 1000)
    else:
        temp.append(max(list(cnt_nums))*100)

print(max(temp))