import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville)   
    
    count = 0
    while scoville[0] < K : 
        count += 1
        
        min_one = hp.heappop(scoville)  
        min_two = hp.heappop(scoville)  
        hp.heappush(scoville, min_one + min_two*2)
        
        if (len(scoville) == 2) and (scoville[0] + scoville[1]*2) < K: 
            return -1  
        
    return count

# 정렬을 매번 반복문마다 하니 시간초과
# 힙을 사용하면 알아서 정렬을 해주므로 시간복잡도가 줄어든다.

# # heapq 라이브러리 호출
# import heapq as hp

# # 사용 가능한 heapq 라이브러리 모듈
# hp.heapify(x)			# 리스트 x를 힙으로 반환한다.

# hp.heappush(heap, item)		# item 값을 heap으로 push한다.
# hp.heappop(heap)		# heap에서 가장 작은 값을 pop한다(=빼낸다).
# hp.heappushpop(heap, item)	# heap에 item을 push한 후, heap에서 가장 작은 값을 pop한다. (개별 호출하는 것보다 더 효율적)
# hp.heapreplace(heap, item)	# heap에서 가장 작은 값을 pop한 후, 새로운 item을 push한다. (개별 호출하는 것보다 더 효율적)

# # 힙에서 최소값을 삭제하지 않고, 얻으려고 할 때 사용 가능한 방법
# # 주의! 두번째로 작은 원소를 얻으려면 바로 heap[1]으로 접근하면 안된다.
# # 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문! 
# # 따라서, 반드시 heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]를 통해 새로운 최소값에 접근해야 한다.
# heap[0]