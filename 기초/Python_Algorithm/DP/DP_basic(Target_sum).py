"""
https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.


This post will walk you through the THINKING process behind Dynamic Programming so that you can solve these questions on your own.

Category
Most dynamic programming questions can be boiled down to a few categories. It's important to recognize the category because it allows us to FRAME a new question into something we already know. Frame means use the framework, not copy an approach from another problem into the current problem. You must understand that every DP problem is different.

Question: Identify this problem as one of the categories below before continuing.

0/1 Knapsack
Unbounded Knapsack
Shortest Path (eg: Unique Paths I/II)
Fibonacci Sequence (eg: House Thief, Jump Game)
Longest Common Substring/Subsequeunce
Answer: 0/1 Knapsack

Why 0/1 Knapsack? Our 'Capacity' is the target we want to reach 'S'. Our 'Items' are the numbers in the input subset and the 'Weights' of the items are the values of the numbers itself. This question follows 0/1 and not unbounded knapsack because we can use each number ONCE.

What is the variation? The twist on this problem from standard knapsack is that we must add ALL items in the subset to our knapsack. We can reframe the question into adding the positive or negative value of the current number to our knapsack in order to reach the target capacity 'S'.

States
What variables we need to keep track of in order to reach our optimal result? This Quora post explains state beautifully, so please refer to this link if you are confused: www.quora.com/What-does-a-state-represent-in-terms-of-Dynamic-Programming

Question: Determine State variables.
Hint: As a general rule, Knapsack problems will require 2 states at minimum.

Answer: Index and Current Sum
Why Index? Index represents the index of the input subset we are considering. This tells us what values we have considered, what values we haven't considered, and what value we are currently considering. As a general rule, index is a required state in nearly all dynamic programming problems, except for shortest paths which is row and column instead of a single index but we'll get into that in a seperate post.

Why Current Sum? The question asks us if we can sum every item (either the positive or negative value of that item) in the subset to reach the target value. Current Sum gives us the sum of all the values we have processed so far. Our answer revolves around Current Sum being equal to Target.

Decisions
Dynamic Programming is all about making the optimal decision. In order to make the optimal decision, we will have to try all decisions first. The MIT lecture on DP (highly recommended) refers to this as the guessing step. My brain works better calling this a decision instead of a guess. Decisions will have to bring us closer to the base case and lead us towards the question we want to answer. Base case is covered in Step 4 but really work in tandem with the decision step.

Question: What decisions do we have to make at each recursive call?
Hint: As a general rule, Knapsack problems will require 2 decisions.

Answer: This problem requires we take ALL items in our input subset, so at every step we will be adding an item to our knapsack. Remember, we stated in Step 2 that "The question asks us if we can sum every item (either the positive or negative value of that item) in the subset to reach the target value." The decision is:

Should we add the current numbers positive value
Should we add the current numbers negative value
As a note, knapsack problems usually don't require us to take all items, thus a usual knapsack decision is to take the item or leave the item.

Base Case
Base cases need to relate directly to the conditions required by the answer we are seeking. This is why it is important for our decisions to work towards our base cases, as it means our decisions are working towards our answer.

Let's revisit the conditions for our answers.

We use all numbers in our input subset.
The sum of all numbers is equal to our target 'S'.
Question: Identify the base cases.
Hint: There are 2 base cases.

Answer: We need 2 base cases. One for when the current state is valid and one for when the current state is invalid.

Valid: Index is out of bounds AND current sum is equal to target 'S'
Invalid: Index is out of bounds
Why Index is out of bounds? A condition for our answer is that we use EVERY item in our input subset. When the index is out of bounds, we know we have considered every item in our input subset.

Why current sum is equal to target? A condition for our answer is that the sum of using either the positive or negative values of items in our input subet equal to the target sum 'S'.

If we have considered all the items in our input subset and our current sum is equal to our target, we have successfully met both conditions required by our answer.

On the other hand, if we have considered all the items in our input subset and our current sum is NOT equal to our target, we have only met condition required by our answer. No bueno.

Code it
If you've thought through all the steps and understand the problem, it's trivial to code the actual solution.

 def findTargetSumWays(self, nums, S):
     index = len(nums) - 1
     curr_sum = 0
     return self.dp(nums, S, index, curr_sum)
     
 def dp(self, nums, target, index, curr_sum):
 	# Base Cases
     if index < 0 and curr_sum == target:
         return 1
     if index < 0:
         return 0 
     
 	# Decisions
     positive = self.dp(nums, target, index-1, curr_sum + nums[index])
     negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
     
     return positive + negative
Optimize
Once we introduce memoization, we will only solve each subproblem ONCE. We can remove recursion altogether and avoid the overhead and potential of a stack overflow by introducing tabulation. It's important to note that the top down recursive and bottom up tabulation methods perform the EXACT same amount of work. The only different is memory. If they peform the exact same amount of work, the conversion just requires us to specify the order in which problems should be solved. This post is really long now so I won't cover these steps here, possibly in a future post.

Memoization Solution for Reference

class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum)
        
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]
Leave a comment on what DP problems you would like this type of post for next and upvote this solution if you found it helpful. I'd like to get this to the top because I'm honestly tired of seeing straight optimized tabulated solutions with no THINKING process behind it.

DP IS EASY!

Thanks.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {} # 메모리에 status를 저장한다.
        
        def dp(nums, index, curr_sum): # 각 부분 문제에 대한 알고리즘
            # 메모리 읽기 -> 미리 저장된 중복 부분 문제 답을 호출 
            if (index,curr_sum) in self.memo:
                return self.memo[(index,curr_sum)]
            # baseline
            if(index<0 and curr_sum == target):
                return 1
            elif(index<0):
                return 0
            # decision 방법을 모두 정의 
            positive = dp(nums,index-1,curr_sum + nums[index])
            negative = dp(nums,index-1,curr_sum - nums[index])
            self.memo[(index,curr_sum)] = positive + negative
            return self.memo[(index,curr_sum)]
        
        return dp(nums,len(nums)-1,0)
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        exp_set = [sum(nums)]
        for ele in nums:   
            exp_set = exp_set + [s - 2*ele for s in exp_set]
        return exp_set.count(target)
    """         
        
