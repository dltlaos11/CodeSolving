def solution(phone_book):
    
    answer = True
    
    # Hash map
    hash_map = {} 
    for nums in phone_book: 
        try: hash_map[nums] = 1
        except: hash_map[nums] = 0
    
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 본인 제외
            if arr in hash_map and arr != nums:    
                answer = False
                return answer
        
    return answer
# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 구조대 전화번호는 영석이의 전화번호의 접두사
# 구조대 : 119
# 지영석 : 11 9552 4421

# 전화번호부에 적힌 전화번호를 담은 배열 phone_book
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
# 그렇지 않으면 true를 return 