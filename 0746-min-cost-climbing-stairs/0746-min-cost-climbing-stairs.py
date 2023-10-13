class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1] , dp[i-2])
            
        """
        Now, we return min(dp[-1], dp[-2])
        It may happen that we reach -2th position and we do not need to take anything from the cost
        """
        
        return min(dp[-1], dp[-2])
        