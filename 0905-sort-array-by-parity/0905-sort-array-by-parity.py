class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums)-1
        while end>start:
            if nums[start]%2 == 0 and nums[end]%2 == 1:
                ## we are good and move ahead
                start, end = start+1, end-1
            elif nums[start]%2 == 1 and nums[end]%2 == 0:
                ## just swap them
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1
            elif nums[start]%2 == 0 and nums[end]%2 == 0:
                ## we are good with start, so move the start pointer only
                start = start+1
            elif nums[start]%2 == 1 and nums[end]%2 == 1:
                ## we move the end pointer as that is okay
                end = end-1
        return nums
                
        