n, m = map(int, input().split())
counter = {}
result = []
for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i+j
        if sum in counter:
            counter[sum] += 1
        else:
            counter[sum] = 1
max_val = max(counter.values())
for key, val in counter.items():
    if val == max_val:
        result.append(key)

print(' '.join(map(str, result)))