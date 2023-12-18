from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    visited = [False] * len(words)    
    
    def bfs(wd, depth):
        nonlocal answer
        queue.append([wd, depth])    # [단어, 깊이]
        
        while queue:
            word, cnt = queue.popleft()
            
            if word == target:
                answer = cnt
                break        
                
            for i in range(len(words)):
                temp = 0
                if not visited[i]:
                    # 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            print(word, word[j], words[i][j], j)
                            temp += 1

                    if temp == 1:   # 만약 다른 글자 개수가 1개라면
                        queue.append([words[i], cnt+1])
                        print(queue)
                        visited[i] = True
                        print(visited)
    bfs(begin, 0)
    return answer