"""
https://leetcode.com/problems/subsets/


* 연산은 리스트에 포함된 원소를 풀어주는 역활을 한다.

"""



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [[], nums]
        
        s = self.subsets(nums[1:])  # nums[0]를 기준으로 자신을 제외한 subset을 만듦.
        
        return [*[[nums[0]] + s_e for s_e in s], *s] # nums[0]를 포함한 subset과 아닌 subset를 합쳐서 반환