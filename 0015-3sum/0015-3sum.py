class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        We sort the nums, so that duplicates can be removed easily
        Now, we iterate through the left for the first num, then on the remaining part, 
        with two pointers, we search for the zero sum
        """
        nums.sort()
        ans = []
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total>0:
                    right = right-1 ## we have to decrease the total
                elif total<0:
                    left = left+1 ## we have to increase the total
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left, right = left+1, right-1
                    while (nums[left] == nums[left-1]) and left<right:
                        left = left+1
                        ## This last part ensures that the second element is also
                        ## not duplicated. 
        
        return ans                
        