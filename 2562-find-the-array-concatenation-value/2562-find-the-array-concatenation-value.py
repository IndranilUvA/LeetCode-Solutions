class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        ans = 0
        if len(nums)%2 !=0:
            ans = ans + nums[len(nums)//2]
        
        first, last = 0, len(nums)-1
        while first<last:
            ans = ans + int(str(nums[first]) + str(nums[last]))
            first, last = first+1, last-1
        return ans
        
        
        