class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #before that single num: odd index and even index have same number
        #after that single num: even index and odd index have same number
        #Binary Search
        #if mid,mid-1 are different and mid, mid+1 are different then we know mid is the answer
        #now if mid and mid+1 are same, then we know that we search in the left
        # we know that the initial size of the array is always odd
        ## if mid and mid+1 are same or mid and mid-1 are same
        ## then we remove those two and then one side has odd number of observations and one side has even number of observations
        ## We always search again in the side where the size is odd
        
        start, end = 0, len(nums)-1
        
        if len(nums) == 1: return nums[0]
        
        ## edge cases: the unique number is at the extreme left or extreme right
        if nums[start]!=nums[start+1]: return nums[start]
        if nums[end]!=nums[end-1]: return nums[end]
        
        while start<=end:
            mid = (start+end)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid] == nums[mid-1]:
                ## we remove these two numbers and then the leftsize is mid-1 (0,1,...,mid-2)
                leftsize = mid-1
                ## now if leftsize is odd, then we search in the left otherwise we search in the right
            else:
                leftsize = mid
            
            if leftsize%2 == 0:
                start = mid+1
            else:
                end = mid-1
                
            
        