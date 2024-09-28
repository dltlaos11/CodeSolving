n = int(input())
scores = list(map(int, input().split()))
avg = int(round(sum(scores) / n, 0))
minTemp = list(map(lambda i: abs(i - avg), scores))
min = abs(min(minTemp))
compare = []

for i in range(1, len(scores)+1):
    val = abs(avg - scores[i-1])
    if val == min:
        compare.append(i)

for i in compare:
    if avg > scores[i-1]:
        compare.remove(i)

print(avg, compare[0])