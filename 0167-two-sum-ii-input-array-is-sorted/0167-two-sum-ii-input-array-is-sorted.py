class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left<right:
            temp = nums[left] + nums[right]
            if temp == target:
                return [left+1, right+1]
            if temp>target:
                ## We need to decrease temp, so
                right = right - 1
            if temp<target:
                ## increase temp
                left = left + 1
        
                
        