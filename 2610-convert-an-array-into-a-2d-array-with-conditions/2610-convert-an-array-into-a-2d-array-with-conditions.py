class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] = freq_dict[i] + 1
            else:
                freq_dict[i] = 1
        
        max_freq = max(freq_dict.values())
        
        for freq in range(1, max_freq+1):
            temp = []
            for k,v in freq_dict.items():
                if v>=freq:
                    temp.append(k)
            ans.append(temp)
        return ans
            
            