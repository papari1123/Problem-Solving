"""
https://programmers.co.kr/learn/courses/30/lessons/42628

1. max, min heap을 만든다.
2. 동기화 시키되, remove를 활용.
3. max heap은 tuple이용해서 접근
"""

import heapq as hq
def solution(operations):
    minheap = []
    maxheap = []
    for oper in operations:
        if oper[0] == 'I':
            item = int(oper[2:])
            print(item)
            hq.heappush(minheap,item)
            hq.heappush(maxheap,(-item,item))
        elif len(minheap) == 0:
            continue
        elif oper[2] == '1': # max
            max_ = hq.heappop(maxheap)[1]  
            minheap.remove(max_)
        else: #min
            min_ = hq.heappop(minheap)
            print(min_)
            maxheap.remove((-min_,min_))
    if(len(minheap)):
        return [maxheap[0][1],minheap[0]]
    else:
        return [0,0]