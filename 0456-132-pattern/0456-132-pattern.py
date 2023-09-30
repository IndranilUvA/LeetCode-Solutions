class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ## We create a minmum so far list
        ## then, we traverse the original array from right for potential j
        ## if nums[ind]>minlist[ind] then ind is a potential candidate for j
        ## we do not need to find i because we know that already the i exists
        ## For potential k, we create a stack. 
        ## if top most element of stack is bigger than j th candidate, then we pop that element 
        ## as that can not be a k
        ## otherwise, we return True
        
        minlist = [nums[0]]
        min_so_far = nums[0]
        for i in range(1, len(nums)):
            min_so_far = min(min_so_far, nums[i])
            minlist.append(min_so_far)
            
        print(minlist)
        
        stack = []
        for ind in range(len(nums)-1, -1, -1):
            if nums[ind]>minlist[ind]:
                while stack and stack[-1]<=minlist[ind]:
                    stack.pop()
                if stack and stack[-1]<nums[ind]:
                    return True
            stack.append(nums[ind])
        
        return False
                
                
            
        