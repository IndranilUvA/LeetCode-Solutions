class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = {}
        for ch in chars:
            if ch in chars_freq:
                chars_freq[ch] = chars_freq[ch] + 1
            else:
                chars_freq[ch] = 1
                
        temp_freq = {}
        ans = 0
        
        def subset(w, chars_freq):
            for ch in w:
                if ch not in chars_freq:
                    return 0
            
            freq = {}
            
            for ch in w:
                if ch in freq:
                    freq[ch] = freq[ch] + 1
                    if freq[ch]>chars_freq[ch]:
                        return 0
                else:
                    freq[ch] = 1
                
            return len(w)
        
        ans = 0
        
        for w in words:
            ans = ans + subset(w, chars_freq)
            
        return ans
            
        
        