

# Bottom up

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
    

# Top down

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for j in range(m+1)]
        def sol(i,j):
            if i >= m or j>=n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            a = sol(i+1,j)
            b = sol(i,j+1)
            dp[i][j] = a+b
            return a+b
        return sol(0,0)
        
        