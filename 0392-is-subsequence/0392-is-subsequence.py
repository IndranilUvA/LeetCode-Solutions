class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s, pointer_t = 0, 0
        
        while pointer_s<len(s) and pointer_t<len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s, pointer_t = pointer_s+1, pointer_t+1
            else:
                pointer_t = pointer_t+1
        
        return pointer_s == len(s)
        