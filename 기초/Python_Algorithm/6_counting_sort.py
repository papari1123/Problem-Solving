"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = [[] for _ in range(20001)]
        
        for l in lists:
            head = l
            
            while head is not None:
                array[head.val + 10000].append(head)
                
                head = head.next
        
        new_list, head = None, None
        
        for a in array:
            for n in a:
                if new_list is None:
                    new_list = n
                    head = n
                else :
                    head.next = n
                    head = head.next
        
        return new_list