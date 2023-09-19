class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return i
            else:
                nums_set.add(i)
                
        
        