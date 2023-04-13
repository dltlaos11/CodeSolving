rand = list(map(int, input().split()))
cnt = 0

for i in range(-1, 2):
    if rand[i] == rand[i+1]:
        cnt += 1

if cnt == 3:
    for i in range(3):
        all_same = rand[i]*1000
    result = all_same + 10000
    print(result)
if cnt == 1:
    if rand.count(rand[0]) == 2:
        two_same = rand[0]*100
        result = two_same + 1000
        print(result)
    else:
        two_same = rand[1]*100
        result=two_same + 1000
        print(result)
if cnt == 0:
    one_same = max(rand)*100
    print(one_same)
