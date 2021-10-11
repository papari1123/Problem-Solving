
"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
"""

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        q = []
        
        left, right = min([n[0] for n in nums]), max([n[0] for n in nums])
        min_left, min_right = left, right
        
        for i, n in enumerate(nums):
            heappush(q, (n[0], i, 0))
        
        while len(q) == len(nums):
            current = heappop(q)
            
            if current[2] + 1 == len(nums[current[1]]):
                break
                
            new = nums[current[1]][current[2] + 1]
            heappush(q, (new, current[1], current[2] + 1))
            
            right = max(right, new)
            left = q[0][0]
            
            if right - left < min_right - min_left:
                min_right, min_left = right, left
                
        return [min_left, min_right]