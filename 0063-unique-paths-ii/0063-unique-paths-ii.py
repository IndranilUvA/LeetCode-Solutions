class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrow, ncol = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*ncol for _ in range(nrow)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
            
        for i in range(nrow):
            for j in range(ncol):
                if i+j!=0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]
        