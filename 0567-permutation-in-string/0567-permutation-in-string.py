class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Create a freq table for s1 chars
        With the length of s1's slide a window on s2 and keep creating a freq_dict_moving for s2
        Check everytime if that dict is equal to s1's dictionary
        """
        if len(s1)>len(s2): return False
        
        s1_freq = {}
        for i in s1:
            if i in s1_freq:
                s1_freq[i] = s1_freq[i] + 1
            else:
                s1_freq[i] = 1
        
        s2_freq = {}
        
        for j in range(len(s1)):
            if s2[j] in s2_freq:
                s2_freq[s2[j]] = s2_freq[s2[j]] + 1
            else:
                s2_freq[s2[j]] = 1
        
        
        left, right = 0, len(s1)-1
        
        while right<len(s2):
            if s1_freq == s2_freq:
                return True
            s2_freq[s2[left]] = s2_freq[s2[left]]-1
            if s2_freq[s2[left]] == 0:
                del s2_freq[s2[left]]
            
            left, right = left+1, right+1
            if right<len(s2):
                if s2[right] in s2_freq:
                    s2_freq[s2[right]] = s2_freq[s2[right]] + 1
                else:
                    s2_freq[s2[right]] = 1
        return False
        
        