## URL: https://leetcode.com/problems/house-robber/
## Approach: Dynamic Programming
## Explaination:
## We can use a dp array to store the maximum amount of money that can be robbed till the ith house
## The dp array is initialized with -1
## We can use a recursive function to calculate the maximum amount of money that can be robbed till the ith house
## The recursive function takes the index of the house as an argument

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        def rob(i):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = max(nums[i]+rob(i-2), rob(i-1))
            return dp[i]
        return rob(n-1)

        