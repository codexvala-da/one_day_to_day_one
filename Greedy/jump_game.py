#Explanation: 
# 1. We first check if the length of the array is less than 2. If it is, we return True.
# 2. We then initialize two variables m and i to 0.
# 3. We iterate through the array.
# 4. We update m to the maximum of i+nums[i] and m.
# 5. We increment i by 1.
# 6. If m is greater than or equal to the length of the array, we return True.
# 7. Else, we return False.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        m=0
        i=0
        while(i<=m and m<len(nums)):
            m = max(i+nums[i],m)
            i+=1
        if m>=len(nums)-1:
            return True
        return False