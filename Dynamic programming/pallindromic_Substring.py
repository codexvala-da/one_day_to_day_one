#Explaineation :
# 1. We will iterate over the string and for each character we will consider it as the center of the palindrome and expand the window to left and right and check if the characters are equal.
# 2. We will consider two cases:
#     a. When the length of the palindrome is odd
#     b. When the length of the palindrome is even
# 3. We will keep track of the number of palindromes found so far and return the count at the end
# 4. We will also consider the single character as a palindrome and add it to the count
# 5. We will return the count at the end


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for k in range(len(s)):
            i=k-1
            j=k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
                ans+=1
            i=k
            j=k+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
                ans+=1
        return ans+len(s)
        