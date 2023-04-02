class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        temp_dict = {}
        for i in range(1,26):
            temp0 = "0"*i
            temp1 = "1"*i
            temp_dict[i] = temp0+temp1
            
        for i in range(25, 0, -1):
            v = temp_dict[i]
            if v in s:
                return 2*i
        return 0

        
        
        