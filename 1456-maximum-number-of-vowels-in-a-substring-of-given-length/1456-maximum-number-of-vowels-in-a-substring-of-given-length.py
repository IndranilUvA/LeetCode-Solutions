class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        vowel_set = set(vowels)
        count = 0
        for i in range(k):
            if s[i] in vowel_set:
                count = count + 1
        
        first, last = 0, k
        ans = count
        n = len(s)
        while last<n:
            if s[last] in vowel_set and s[first] in vowel_set:
                count = count
            elif s[last] in vowel_set and s[first] not in vowel_set:
                count = count+1
            elif s[last] not in vowel_set and s[first] in vowel_set:
                count = count-1
            else:
                count = count
            first, last = first+1, last+1
            ans = max(ans, count)
        return ans
            
        
            
        