class Solution:
    """
    Just doing what has been told. First we calculate the onesrow and onescol array where it captures 
    the number of ones in each row and column of the matrix. Then we create a new ans matrix. 
    We calculate the elements using these two arrays. Note the number of zeros can easily be calculated 
    if we only have the number of 1s in the array.
    """
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        onesrow, onescol = [0]*m, [0]*n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesrow[i] = onesrow[i] + 1
                    onescol[j] = onescol[j] + 1
        
        diff = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = onesrow[i]
                b = onescol[j]
                c = n-a
                d = m-b
                diff[i][j] = a+b-c-d
        
        return diff