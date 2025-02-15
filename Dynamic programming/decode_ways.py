# Explaination:
# We start with creating a dictionary of all the alphabets and their corresponding numbers.
# We will create a recursive function that will take the index of the string as an argument.
# We will check if the index is greater than the length of the string, then we will return 1.
# If the character at the index is not in the dictionary, then we will return 0.
# We will check if the index is already in the dp dictionary, then we will return the value from the dp dictionary.
# We will create a variable ans and initialize it to 0.
# We will add the result of the recursive function with index + 1 to the ans.
# We will check if the index + 1 is less than the length of the string and the substring from index to index + 2 is in the dictionary, then we will add the result of the recursive function with index + 2 to the ans.
# We will store the ans in the dp dictionary with the index as the key.
# We will return the ans.

class Solution:
    def numDecodings(self, s: str) -> int:
        ans = 0
        d = {}
        for i in range(26):
            d[str(i+1)] = chr(65+(i))
        dp = {}
        def sol(i):
            if i>=len(s):
                return 1
            if s[i] not in d:
                return 0
            if i in dp:
                return dp[i]
            ans = 0
            ans+=sol(i+1)
            if i+1<len(s) and s[i:i+2] in d:
                ans+=sol(i+2)
            dp[i] = ans
            return ans
        return sol(0)
