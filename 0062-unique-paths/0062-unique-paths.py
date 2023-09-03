class Solution:
    """
    A sequence of m+n-2 length with m-1 R (right) and n-1 L (left) is a path
    Hence, the answer is (m+n-2)C(m-1)
    """
    def comb(self, n, r):
        """
        This produces the nCr
        """
        num, denom = 1 , 1
        for i in range(n-r+1, n+1):
            num = num * i
        for j in range(1, r+1):
            denom = denom * j
        
        return num//denom
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.comb(m+n-2, m-1)
        