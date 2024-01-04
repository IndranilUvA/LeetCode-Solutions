class Solution:
    """
    If there is one number x, then its frequqncy can be either 3k, 3k+1 or 3k+2, 
    if the freq is 3k, then we need 3 steps to empy, if 3k+2, we need k+1 steps (k times 3 and one time 2)
    if the freq is 3k+1, then we need k+1 steps(3k+1 = 3(k-1) + 4), so k-1+(1+1) steps. 
    Edge caes: If the freq 1, no solution, if freq 2: one solution no other edge case
    """
    
    def mumops_fromfreq(self, freq):
        if freq == 1:
            return -1
        if freq == 2: return 1
        k, r = freq//3, freq%3
        if r == 0: return k
        return k+1
    
    def minOperations(self, nums: List[int]) -> int:
        
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] = freq_dict[i] + 1
            else:
                freq_dict[i] = 1
                
        ans = 0
        
        for k,v in freq_dict.items():
            temp = self.mumops_fromfreq(v)
            if temp == -1:
                return -1
            ans = ans + temp
        
        return ans