class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        """
        This solution uses O(n) space, O(1) space solution TBD
        """
        
        target = len(nums)/3
        
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
                
                
        ans = []
        for k,v in d.items():
            if v>target:
                ans.append(k)
                
        return ans
        