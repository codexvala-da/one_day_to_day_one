# Explaination :
# Initialize a 2D DP table with -1 (for memoization)
# Size is (n+2) x (n+2) to accommodate indices safely
# Recursive function to find the length of LIS
        # index: current position in the array
        # last: index of the last included element in the increasing subsequence
# If current element is greater than the last included element
            # We have two choices:
            # 1. Include nums[index] in LIS and move forward (increase count by 1)
            # 2. Skip nums[index] and move forward

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Input: nums = [10,9,2,5,3,7,101,18]
        t = [[-1 for i in range(len(nums)+2)] for j in range(len(nums)+2)]
        nums = [-sys.maxsize] + nums
        def sol(index,last):
            if index >= len(nums):
                return 0
    
            if t[index][last]!=-1:
                return t[index][last]
            
            if nums[index]>nums[last]:
                t[index][last] =  max(1 + sol(index+1,index), sol(index+1,last))
            
            else:
                t[index][last] =  sol(index+1,last)

            return t[index][last]
        
        return sol(1,0)

            