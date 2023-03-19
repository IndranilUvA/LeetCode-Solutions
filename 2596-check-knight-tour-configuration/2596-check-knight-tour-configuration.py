class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        start_x, start_y = 0, 0
        moves = [(1,2), (2,1), (1,-2), (-1,2), (-1,-2), (-2,-1), (2,-1), (-2,1)]
        if grid[start_x][start_y]!=0:
            return False
        
        n = len(grid)
        
        for i in range(1, n*n):
            for count, m in enumerate(moves):
                x,y = m
                next_x, next_y = start_x+x, start_y+y
                if 0<=next_x<n and 0<=next_y<n and grid[next_x][next_y] == i:
                    start_x, start_y = next_x, next_y
                    break
                elif count == 7:
                    return False
        return i == n*n-1
                
        
        