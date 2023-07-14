class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        
        """
        dp dictionary. dp[x] denotes the answer till number x from left of the array that includes x
        We iterate the array from left. 
        If x-difference is in dict, then we increase dp[x] = dp[x-difference] + 1
        else dp[x] = 1
        Finally we return the max value from the disctionary
        """
        
        
        dp = {}
        for num in arr:
            if num - diff in dp:
                dp[num] = dp[num-diff] + 1
            else:
                dp[num] = 1
        return max(dp.values())
        