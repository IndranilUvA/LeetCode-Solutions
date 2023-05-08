class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        for i in range(n):
            ans = ans + mat[i][i] + mat[i][n-i-1]
        return ans if n%2==0 else ans - mat[n//2][n//2]
            
            
        