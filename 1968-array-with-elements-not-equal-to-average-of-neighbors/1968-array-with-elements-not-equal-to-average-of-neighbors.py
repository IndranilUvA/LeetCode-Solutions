class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):
            previous, current, next_ = nums[i-1], nums[i], nums[i+1]
            
            ### If these three are either in increasing or decreasing, we just break that ###
            ### We can swap next and current ####
            
            if previous>current>next_ or previous<current<next_:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
        return nums
        