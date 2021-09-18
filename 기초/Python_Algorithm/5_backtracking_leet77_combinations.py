"""
https://leetcode.com/problems/combinations/
"""

from typing import List

"""


"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done1 
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output

class MySolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTracking(value = 0,curr:List[int] = []):
            if len(curr)==self.k:
                self.ans.append(curr[:])
                return curr
            else:
                while value<self.n-k+len(curr)+1:        
                    value += 1
                    curr.append(value)
                    curr = backTracking(value,curr)
                    curr.pop()
                return curr
        self.ans = []
        self.n = n
        self.k = k
        backTracking()
        return self.ans

solution = MySolution()
n, k =  map(int,input().split())
print(solution.combine(n,k))