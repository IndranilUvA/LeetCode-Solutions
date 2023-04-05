## note the sum always stays same
## note the ans is always greater or equal to nums[0]
## in example: [3,7] - we take steps untill it becomes [5,5]
## The problem is equivalent to the following
## find the maximum in cumulative average
## max of 3/1, (3+7)/2, (3+7+1)/3, (3+7+1+6)/4
## since the sum is always same, the max can be minimized only if every number is close to that average
## very tricky problem TBH :D

import math
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            total = total + nums[i]
            ans = max(ans, math.ceil(total/(i+1)))
        return ans
            
        