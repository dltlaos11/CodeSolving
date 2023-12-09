from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    truck_weight_in_bridge = 0 # sum
    
    while bridge:

        truck_weight_in_bridge -= bridge.popleft()
        answer += 1
        
        
        if truck_weights:
            # if sum(bridge) + truck_weights[0] <= weight:            
            if truck_weight_in_bridge + truck_weights[0] <= weight:            
                
                truck_weight_in_bridge += truck_weights[0]
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
            else:
                bridge.append(0)
                 
         
    return answer
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며
# 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
# 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
# 지날 때 1초, 거널 때 1초