class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = freq_dict[num] + 1
            else:
                freq_dict[num] = 1
        
        for k,v in freq_dict.items():
            if v == 1:
                return k
        