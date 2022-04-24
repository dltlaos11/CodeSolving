import sys
num = int(sys.stdin.readline())
result = num
for i in range(num):
    word = sys.stdin.readline()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+2:]:
            result-=1
            break
print(result)

# 안ㄴ영
