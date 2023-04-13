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


# sys 모듈의 sys.stdin.readline()을 사용하여 문제를 다시풀어보았다. 제출 결과 input()을 사용했을 떄보다 120ms => 108ms로 시간이
# 줄어드는 것을 확인 할 수 있었다. 앞으로 input()을 사용하기보단 시간단축을 위해서 sys 모듈을 이용해야 겠다.
# 이번 문제에서 pass, break 순간을 지정해줘야 하는 부분에서 고민을 했다..
