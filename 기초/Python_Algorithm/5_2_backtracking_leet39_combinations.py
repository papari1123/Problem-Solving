from typing import List
"""
https://leetcode.com/problems/combination-sum/solution/

As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. 
The idea is that it incrementally builds candidates to the solutions, 
and abandons a candidate ("backtrack") as soon as it determines that this candidate cannot lead to a final solution

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results

class MySolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates,reverse=True)
        self.ans = []
        self.target = target
        def backTracking(idx=0, combi_sum=0, curr=[]):
            while(idx<len(self.candidates)):            
                if(combi_sum==self.target):
                    self.ans.append(curr[:])
                if(combi_sum>=self.target):
                    return curr
                curr.append(self.candidates[idx])
                combi_sum += curr[-1]
                curr = backTracking(idx,combi_sum,curr) 
                combi_sum -= curr[-1]
                curr.pop()
                idx += 1
            return curr
        backTracking()
        return self.ans

solution = MySolution()
candidates =  map(int,input('candidates:').split())
target = int(input('target:'))
print(solution.combinationSum(candidates,target))