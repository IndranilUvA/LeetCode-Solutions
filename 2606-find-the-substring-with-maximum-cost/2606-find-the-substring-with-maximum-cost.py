class Solution:
    
    def max_subarray_sum(self, nums):
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        all_chars = "abcdefghijklmnopqrstuvwxyz"
        val_dict = {all_chars[i]:i+1 for i in range(26)}
        for index, ch in enumerate(chars):
            val_dict[ch] = vals[index]
        
        ans = 0
        s_val = [val_dict[x] for x in s]
        
        return max(ans, self.max_subarray_sum(s_val))
        