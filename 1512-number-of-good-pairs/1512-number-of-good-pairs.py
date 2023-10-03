class Solution:
    """
    We create a frequency dictionary
    For any num, if the freq is f, then fC2 is the count of good pairs for them
    """
    def nC2(self, n):
        return n*(n-1)//2
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] = freq_dict[i] + 1
        
        if len(freq_dict) == 0:
            return 0
        else:
            return sum([self.nC2(v) for v in freq_dict.values()])