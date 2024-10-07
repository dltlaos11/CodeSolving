n = int(input())

score = list(map(int, input().split()))

tmp = [2]

scores = tmp + score

sum = 0
cnt = 0

for i in range(1, len(scores)):

    if scores[i] == 1:
        sum += 1

        if scores[i] == scores[i-1]:
            cnt +=1
            sum+=cnt

        else:
            cnt = 0

print(sum)