class Solution:
    
    """
    Just find the max and second max and then done
    """
    
    def maxProduct(self, nums: List[int]) -> int:
        maxnum, second_max = max(nums[0], nums[1]), min(nums[0], nums[1])
        
        if len(nums) == 2: return (maxnum-1)*(second_max-1)
        
        for i in range(2, len(nums)):
            if nums[i] > maxnum:
                second_max = maxnum
                maxnum = nums[i]
            elif nums[i] > second_max:
                second_max = nums[i]
        
        return (maxnum-1)*(second_max-1)