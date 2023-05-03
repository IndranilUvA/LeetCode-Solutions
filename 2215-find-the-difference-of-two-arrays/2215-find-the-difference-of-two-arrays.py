class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1),set(nums2)
        first = [i for i in nums1 if i not in nums2]
        second = [i for i in nums2 if i not in nums1]
        return [first, second]
        