class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for index, num in enumerate(nums):
            if n%(index+1) == 0:
                ans = ans + (num*num)
        return ans
        