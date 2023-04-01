class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        temp = [i for i in nums1 if i in nums2]
        if len(temp)>=1:
            return min(temp)
        
        min1, min2 = min(nums1), min(nums2)
        if min1<min2:
            return 10*min1 + min2
        else:
            return 10*min2 + min1
        