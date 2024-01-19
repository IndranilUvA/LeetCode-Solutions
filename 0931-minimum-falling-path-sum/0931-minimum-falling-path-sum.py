class Solution:
    
    """
    This seems like a classic DP problem. For this one, we can just overwrite the original input matrix.
    We move from top to bottom in the matrix and update the elements with what is required, so for every element M[i][j], we just update it with the minimum from (M[i-1][j], M[i-1][j-1], M[i-1][j+1]) and move on.

Note that we do not touch the first row and we move from the second row. Finally once the movement is complete, we need to return the minimum from the last row of the matrix
    """
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrow, ncol = len(matrix), len(matrix[0])
        for i in range(1, nrow):
            for j in range(ncol):
                left_top = matrix[i-1][j-1] if j-1>=0 else float("inf")
                top = matrix[i-1][j]
                right_top = matrix[i-1][j+1] if j+1<ncol else float("inf")
                    
                matrix[i][j] = matrix[i][j] + min(left_top, top, right_top)
                   
        return min(matrix[-1])
        