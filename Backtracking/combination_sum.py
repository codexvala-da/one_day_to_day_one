#Explaination: 

# 1. Sort the candidates list.
# 2. Initialize the answer list.
# 3. Define the recursive function sol.
# 4. If the sum is equal to the target, append the current list to the answer list.
# 5. If the sum is greater than the target, return.
# 6. Iterate through the candidates list.
# 7. Call the recursive function with the current index, sum, and current list.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def sol(i,su,curr):
            if i>=len(candidates):
                if su==target:
                    ans.append(curr)
                return
            if candidates[i]>target-su:
                sol(i+1,su,curr)
            else:
                sol(i,su+candidates[i],curr+[candidates[i]])
                sol(i+1,su,curr)
        sol(0,0,[])
        return ans
        