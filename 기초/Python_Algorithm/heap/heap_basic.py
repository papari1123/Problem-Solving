import heapq

"""
min_heap
heap[k]<= heap[2k+1] and heap[k]<= heap[2k+2]

python에서는 heapq 모듈을 통해 삽입, 삭제한 리스트가 min heap임

알아두어야 할 것
1. import heapq를 통해 heqp 모듈을 추가
2. heapq.heapify 또는 heapq.heappush를 통해 리스트를 힙으로 만들거나 원소를 힙에 추가 * heapify:O(n)
3. heapq.heappop 을 통해 최소 원소 제거 또는 힙의 0번쨰 원소 접근
4. max heap을 만드려면 원소에 tuple로 저장하고 key를 음수로 줌. 
"""
heap = []


# 원소 입력 : heapq.heappush
heapq.heappush(heap,1) # 1입력
heapq.heappush(heap,3) # 3입력
heapq.heappush(heap,5)
heapq.heappush(heap,2)
print(heap)

# 원소 삭제 : heapq.heappopp
print(heapq.heappop(heap)) # 가장 작은 값 반환

# 최상위 원소(min 값) 접근
print(heap[0]) # 원소가 삭제되지는 않음.

# 기존 리스트를 힙으로 변환 * 힙이 반환되는 것이 아니라 해당 리스트가 힙조건을 만족하도록 바뀜
test = [1,4,2,4,5,3,1,3,7]
heapq.heapify(test)
print(test)

# max 힙 : 튜플을 원소로 추가 시, 맨 앞에 있는 값만 우선순위가 됨.
test2 = [1,5,7,3,2,5,3,6,5,8]
heap = []
for num in test2:
    heapq.heappush(heap,(-num,num))  ## (우선순위, 값)

