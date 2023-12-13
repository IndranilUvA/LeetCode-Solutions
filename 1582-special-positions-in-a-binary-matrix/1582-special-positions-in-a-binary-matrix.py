class Solution:
    
    """
    In the first pass, we traverse the matrix and compute the rowsum and colsum
    Next, we again traverse the matrix and check if the rowsum and colsum both 1 along with mat[i][j] = 1
    Then we just add those instances and finally return
    """
    
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        rowsum, colsum = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowsum[i] = rowsum[i] + 1
                    colsum[j] = colsum[j] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if rowsum[i]*colsum[j] == 1:
                        ans = ans + 1
        
        return ans
        
        