class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<=2: return True
        if nums[0]<nums[-1]:
            ## if monotonic: the array should be increasing ##
            for i in range(1, len(nums)):
                if nums[i]<nums[i-1]:
                    return False
            return True
        
        if nums[0]>nums[-1]:
            ## if monotomic: the array should be decreasing
            for i in range(1, len(nums)):
                if nums[i]>nums[i-1]:
                    return False
            return True
        
        if nums[0] == nums[-1]:
            if len(set(nums))!=1:
                return False
            return True
                
        