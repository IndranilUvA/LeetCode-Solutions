class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        """
        For non-travel days, the cost stays the same as for the previous day. For travel days, it's a minimum of yesterday's cost plus               single-day ticket, or cost for 8 days ago plus 7-day pass, or cost 31 days ago plus 30-day pass.
        
        Create dp list for every possible day., with zeros, to make that 1-indexed the length can be 1+max_days.
        """
        
        
        max_days = days[-1]
        dp = [0]*(max_days+1)
        
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[max(i-1,0)] + costs[0], 
                            dp[max(i-7,0)] + costs[1],
                            dp[max(i-30,0)] + costs[2])
                
            if i not in days:
                dp[i] = dp[i-1]
        return dp[-1]
            
        
        