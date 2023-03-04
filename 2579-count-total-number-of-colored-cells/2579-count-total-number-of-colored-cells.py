class Solution:
    def coloredCells(self, n: int) -> int:
        """
        When n=4, then we have 7 squares in between, then 5 in both side, 3 in in both sides, 1 in two extremes
        For n=k, in middle we have 2k-1 boxes, then 2k-3, 2k-5,...,1 box at both side
        Answer = 1+3+5+...+(2k-1)+(2k-3)+(2k-5)+...+1 = 2(1+3+5+...+(2k-1))-(2k-1) = 2K^2-(2k-1)
        """
        if n==1: return 1
        return 2*n*n - (2*n-1)
        
        
        