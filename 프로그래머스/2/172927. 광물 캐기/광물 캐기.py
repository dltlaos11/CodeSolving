import sys

def solution(picks, minerals):
    answer = sys.maxsize
    
    # 피로도 테이블: tired_list[곡괭이타입][광물타입]
    tired_list = [
        [1, 1, 1],    # 다이아몬드 곡괭이
        [5, 1, 1],    # 철 곡괭이  
        [25, 5, 1]    # 돌 곡괭이
    ]
    
    # 광물 타입을 인덱스로 매핑
    mineral_to_idx = {"diamond": 0, "iron": 1, "stone": 2}
    
    visited = [0] * 3  # 각 곡괭이 타입별 사용 개수
    orders = []        # 곡괭이 사용 순서
    
    def calc(depth):
        """depth번째 곡괭이로 광물을 캤을 때의 피로도 계산"""
        plus = 0
        pick_type = orders[depth]
        
        # depth번째 곡괭이로 캘 수 있는 광물 범위: [depth*5, (depth+1)*5)
        for i in range(depth * 5, min((depth + 1) * 5, len(minerals))):
            mineral_type = mineral_to_idx[minerals[i]]
            plus += tired_list[pick_type][mineral_type]
        
        return plus
    
    def dfs(depth, tired):
        nonlocal answer
        
        # 모든 곡괭이를 사용했거나 모든 광물을 캤으면 종료
        if depth == sum(picks) or depth * 5 >= len(minerals):
            answer = min(answer, tired)
            return
        
        # 가지치기: 현재 피로도가 이미 최소값보다 크면 중단
        if tired >= answer:
            return
        
        # 각 곡괭이 타입 시도
        for pick_type in range(3):
            if visited[pick_type] < picks[pick_type]:
                visited[pick_type] += 1
                orders.append(pick_type)
                
                plus = calc(depth)
                
                # 가지치기: 미리 체크
                if tired + plus < answer:
                    dfs(depth + 1, tired + plus)
                
                # 백트래킹
                visited[pick_type] -= 1
                orders.pop()
    
    dfs(0, 0)
    return answer