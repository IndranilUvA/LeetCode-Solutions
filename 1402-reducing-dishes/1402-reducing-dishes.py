class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        # nice explanation here: https://leetcode.com/problems/reducing-dishes/discuss/563384/JavaC%2B%2BPython-Easy-and-Concise
        # example: [-1,-8,0,5,-9]
        # After sorting: [-9,-8, -1, 0, 5]
        # we run from the right and keep traversing untill the total dish becomes negative
        # ans = ans + total makes sure that the 5 at the right is multiplied by 3 as that's the time for satisfaction = 5
        # sorting and keeping the max at the right and adding it as much as we can is the idea
        # when the total becomes negative it would start reducing the ans, so we stop there 
        
        satisfaction.sort()
        ans = 0
        total = 0
        
        while satisfaction and satisfaction[-1] + total > 0:
            dish = satisfaction.pop()
            total = total + dish
            ans = ans + total
            
        return ans
            
        