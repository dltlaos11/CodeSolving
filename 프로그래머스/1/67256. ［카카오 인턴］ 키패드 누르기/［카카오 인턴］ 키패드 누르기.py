def solution(numbers, hand):
    keypad = [
        [3, 1],  # 0
        [0, 0], [0, 1], [0, 2],  
        [1, 0], [1, 1], [1, 2],  
        [2, 0], [2, 1], [2, 2]   
    ]
    
    left_keys = {1, 4, 7}
    right_keys = {3, 6, 9}
    
    left_pos = [3, 0]   
    right_pos = [3, 2]  
    
    answer = []
    is_right_hand = hand == 'right'
    
    for num in numbers:
        if num in left_keys:
            answer.append('L')
            left_pos = keypad[num]
        elif num in right_keys:
            answer.append('R')
            right_pos = keypad[num]
        else:
            # Manhattan
            target = keypad[num]
            left_dist = abs(left_pos[0] - target[0]) + abs(left_pos[1] - target[1])
            right_dist = abs(right_pos[0] - target[0]) + abs(right_pos[1] - target[1])
            
            if left_dist < right_dist or (left_dist == right_dist and not is_right_hand):
                answer.append('L')
                left_pos = target
            else:
                answer.append('R')
                right_pos = target
    
    return ''.join(answer)