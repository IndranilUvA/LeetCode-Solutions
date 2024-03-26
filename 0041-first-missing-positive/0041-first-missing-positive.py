class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        The answer should be something between 1,2,..., n+1
        where n is the length of nums. The answer can not be anything beyond that
        """
        nums = set(nums)
        
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i