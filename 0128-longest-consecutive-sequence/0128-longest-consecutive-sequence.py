class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Assume the numbers in a number line. Then we have three groups from the example
        [1,2,3,4], [100], [200]
        Now ceck if a number can be the first number in the sequence
        n can be the start of a sequence only if n-1 is not in nums
        That way we only have 1, 100 and 200. Now count from them.
        """
        nums = set(nums)
        
        max_length = 0
        
        for n in nums:
            if n-1 not in nums:
                length = 1
                while n + length in nums:
                    length = length + 1
                max_length = max(max_length, length)
        return max_length
                
        