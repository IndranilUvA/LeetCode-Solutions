class Solution:
    """
    This is a typical binary search problem. 
    The basic template to find a unique number index in sorted array: [1, 2, 4, 4, 6, 7, 8] and target: 7
    We do 
    while left<=right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[mid]<target:left = mid+1
        if nums[mid]>target: right = mid-1
    return mid
    Now, since the target appears multiple times, we do not stop if the mid is target
    For the leftmostindex, we just update the variable and move the right pointer there and the vice versa
    This is when we have multiple target present in the array and we want to find either the leftmost and rightmost occurance    
    """
    def leftmosttarget(self, nums, target):
        left, right = 0, len(nums)-1
        leftmost_index = -1
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                leftmost_index = mid
                right = mid-1
            if nums[mid]<target:
                left = mid+1
            if nums[mid]>target:
                right = mid-1
                
        return leftmost_index
    
    def rightmosttarget(self, nums, target):
        left, right = 0, len(nums)-1
        rightmost_index = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                rightmost_index = mid
                left = mid+1
            if nums[mid]<target:
                left = mid+1
            if nums[mid]>target:
                right = mid-1
        return rightmost_index
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans_left, ans_right = self.leftmosttarget(nums, target), self.rightmosttarget(nums, target)
        return [ans_left, ans_right]
    
        