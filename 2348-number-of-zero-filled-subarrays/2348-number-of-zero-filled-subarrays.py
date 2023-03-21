class Solution:
    def run_sum(self, n):
        #### if a sub=array has n consecutive zeros, we have n(n+1)/2 total number of sub-arrays filled with zeros ####
        return n*(n+1)//2
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, right = 0, 1
        ans = 0
        while right<len(nums):
            if nums[left] == 0 and nums[right] == 0:
                right = right + 1
            elif nums[left] == 0 and nums[right]!=0:
                zero_run = right-left
                ans = ans + self.run_sum(zero_run)
                left = right+1
                right = right+2    
            elif nums[left]!= 0  and nums[right]!=0:
                left, right = left+1, right+1
            elif nums[left]!=0 and nums[right]==0:
                left = right
                right = right+1
                
        if nums[-1] == 0:
            ans = ans + self.run_sum(len(nums)-left)
        
        return ans