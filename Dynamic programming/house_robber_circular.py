# Explanation:
# We can solve this problem by considering two cases:
# 1. We rob the first house and don't rob the last house
# 2. We don't rob the first house and rob the last house
# We can solve the above two cases by calling the rob function twice with different arguments
# We can then return the maximum of the two cases

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)
        def sol(i,nums):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            else:
                dp[i] = max(nums[i]+sol(i-2,nums),sol(i-1,nums))
            return dp[i]
        dp = [-1 for i in range(n)]
        a = sol(n-2,nums[:-1])
        dp = [-1 for i in range(n)]
        b= sol(n-2,nums[1:])
        return (max(a,b))

        