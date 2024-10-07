n = int(input())

def check_reverse(x):
    tmp = len(x) // 2
    if len(x) % 2 == 0:
        left = x[:tmp]
        right = x[tmp:]
    else:
        left = x[:tmp]
        right = x[-tmp:]

    result = 'YES' if left == right[::-1] else 'NO'
    return result

for i in range(1, n+1):
    word = str(input()).lower()
    print(f"#{i} {check_reverse(word)}")