import heapq as hq
"""
https://programmers.co.kr/learn/courses/30/lessons/42626
"""

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while(scoville[0]<K and len(scoville)>1):
        a1 = hq.heappop(scoville)
        a2 = hq.heappop(scoville)
        hq.heappush(scoville, a1 + a2*2)
        answer += 1
    if(scoville[0]<K):
        return -1
    return answer