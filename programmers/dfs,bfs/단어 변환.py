from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    visited = [False] * len(words)    # 방문 노드 여부 확인 리스트
    
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
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            temp += 1

                    if temp == 1:   # 만약 다른 글자 개수가 1개라면
                        queue.append([words[i], cnt+1])
                        visited[i] = True
    bfs(begin, 0)
    return answer