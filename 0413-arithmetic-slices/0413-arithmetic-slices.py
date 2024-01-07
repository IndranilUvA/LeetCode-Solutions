class Solution:
    
    """
    dp[i]: number of AP subarrays till index i,
    we finally sum all these elements for all i and return
    """
    
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return 0
        
        dp = [0]*len(nums)
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] + 1
        print(dp)       
        return sum(dp)
                
                
        