class Solution:
    
    """
    We sort every word, if anagram the words should have the same sorted word
    """
    
    def sorted_word(self, word):
        return "".join(sorted(list(word)))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """
        Create a dictionary and the sorted words are keys and the originals words are in values within a list
        """
        
        d = {}
        
        for w in strs:
            temp = self.sorted_word(w)
            if temp in d:
                d[temp].append(w)
            else:
                d[temp] = [w]
                
        return list(d.values())
        
        