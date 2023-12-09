from itertools import product

def solution(words):
    answer = 0
    
    result = []
    for i in range(1, 6):
        word = list(product(["A", "E", "I", "O", "U"], repeat=i)) # 중복순열
        for wrd in word:
            result.append(''.join(wrd))
        
    result.sort()
    answer = result.index(words) + 1

    return answer

# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return