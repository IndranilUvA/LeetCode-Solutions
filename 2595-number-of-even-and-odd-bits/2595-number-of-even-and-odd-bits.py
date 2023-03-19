class Solution:
    def dec_to_bin(self, num):
        if num == 0: return 0
        if num == 1: return [1]
        ans = []
        while num//2>0:
            q, r = num//2, num%2
            num = q
            ans.append(r)
        ans.append(q)
        #ans.reverse()  ## originally, we should reverse this, but here 0th index for a binary number is the right most one ##
        return ans
        
    def evenOddBit(self, n: int) -> List[int]:
        binary = self.dec_to_bin(n)
        even, odd = 0, 0
        for i,j in enumerate(binary):
            if i%2 == 0 and j == 1:
                even = even + 1
            if i%2 == 1 and j == 1:
                odd = odd + 1
        return [even, odd]
        