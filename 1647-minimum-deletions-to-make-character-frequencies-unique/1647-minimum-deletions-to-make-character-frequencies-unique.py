class Solution:
    """
    We create a frequency dictionary for string s
    Now, we create a set of unique values of the freq_dict
    We create an empty set, eventually this contains the unique frequency of characters in s
    we loop through the dictionary keys (unique characters of s)
    If the frequency is matched with some older frequency in the set, we keep decreasing it and add it to ans
    We update every time the unique_values set
    """
    def freq_dict(self, s):
        d = {}
        for ch in s:
            if ch in d:
                d[ch] = d[ch] + 1
            else:
                d[ch] = 1
        return d
                
    
    def minDeletions(self, s: str) -> int:
        fr_dict = self.freq_dict(s)
        unique_values = set()
        ans = 0
        
        for ch, freq in fr_dict.items():
            while freq>0 and freq in unique_values:
                freq = freq - 1
                ans = ans + 1
            unique_values.add(freq)
        return ans
        
                
                
            
        