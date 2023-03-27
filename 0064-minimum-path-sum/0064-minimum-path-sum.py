class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        ## First we copy the original matrix ##
        ##nOte: the first element would never change: dp[0][0]
        m,n = len(grid), len(grid[0])
        
        ## For the first row and the first column we just have to add the previous row element or the previous column element
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + dp[i][0]
            
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + dp[0][j]
            
            
        ## For the other elements, dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + dp[i][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + dp[i][j]
        
        return dp[-1][-1]
        