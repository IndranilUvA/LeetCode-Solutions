class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = {}
        dp[0], dp[1] = [1], [1,1]
        
        if rowIndex < 2:
            return dp[rowIndex]
        
        for i in range(2, rowIndex+1):
            dp[i] = [1]*(i+1)
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
        return dp[rowIndex]