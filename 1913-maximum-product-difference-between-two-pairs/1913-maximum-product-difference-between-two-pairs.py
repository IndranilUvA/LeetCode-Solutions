class Solution:
    """
    We need to sort the array, then first two elements and and last two elements are the candidate
    Note this way the time complexity is O(nlogn)
    We can also find the max and second max and min and second min in O(n) time and then find the ans
    """
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2]) - (nums[1]*nums[0])