class Solution:
    
    """
    One quickt and dirty pythonic colution is list(zip(*matrix))
    However, we create a matrix: ans, with swappning the size of num rows and columns and do basic transpose task
    It takes O(mn) time and space. Note that in space is impossible, as ans and matrix are of different sie, as matrix is 
    not square
    """
    
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        nrows, ncols = len(matrix), len(matrix[0])
        
        ans = [[None]* nrows for _ in range(ncols)]
        
        for i in range(nrows):
            for j in range(ncols):
                ans[j][i] = matrix[i][j]
                
        return ans
        