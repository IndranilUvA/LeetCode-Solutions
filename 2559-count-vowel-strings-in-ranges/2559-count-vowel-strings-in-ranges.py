class Solution:
    
    def first_last_vowel(self, word):
        if word[-1] in set("aeiou") and word[0] in set("aeiou"):
            return True
        return False
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        cum_sum_dict={i:0 for i in range(len(words))}
        # cum_sum_dict[i]: number of words with first and last vowel upto index i (included)
        temp_sum = 0
        for i in range(len(words)):
            if self.first_last_vowel(words[i]):
                temp_sum = temp_sum + 1
            cum_sum_dict[i] = temp_sum
        
        ans = []
        for i in range(len(queries)):
            left, right = queries[i]
            if left == right:
                if self.first_last_vowel(words[left]):
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                if left != 0:
                    temp_ans = cum_sum_dict[right] - cum_sum_dict[left-1]
                    ans.append(temp_ans)
                if left == 0:
                    temp_ans = cum_sum_dict[right]
                    ans.append(temp_ans)
        
        return ans            
                    
        
        