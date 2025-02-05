# Explaination: https://leetcode.com/problems/contains-duplicate/
# we can use set to remove duplicates and then compare the length of the set with the length of the list
# if they are equal then there are no duplicates else there are duplicates

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not(len(set(nums))==len(nums))