class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        concat s and t and then cound the character frequency
        Only one letter would have odd frequency
        """
        new_ch = s+t
        d = {}
        for ch in new_ch:
            if ch in d:
                d[ch] = d[ch] + 1
            else:
                d[ch] = 1
                
        for k,v in d.items():
            if v%2!=0:
                return k