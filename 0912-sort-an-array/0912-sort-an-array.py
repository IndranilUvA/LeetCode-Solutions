class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] = freq_dict[i] + 1
            else:
                freq_dict[i] = 1
                
        min_num, max_num = min(nums),max(nums)
        ans = []
        for num in range(min_num, max_num + 1):
            if num in freq_dict:
                ans.extend([num]*freq_dict[num])
        return ans