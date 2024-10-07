word = str(input())

tmp = []

for i in word:
    if i.isdigit():
        tmp.append(i)

num = int(''.join(tmp))
count = 0
def count_divisors(n):
    global count
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print(num)
print(count_divisors(num))

