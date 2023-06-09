class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        all_chars = "abcdefghijklmnopqrstuvwxyz"
        
        all_chars_dict = {ch:index for index, ch in enumerate(all_chars)}
        
        target_num = all_chars_dict[target]
        
        ans, ans_index = letters[0], 26 
        
        for ch in letters:
            if all_chars_dict[ch]>target_num and all_chars_dict[ch]<ans_index:
                ans_index = all_chars_dict[ch]
                ans = ch
                
        return ans
                
            
        