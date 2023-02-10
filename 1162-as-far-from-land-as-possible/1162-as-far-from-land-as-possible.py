from collections import deque 
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Basically, every step towards right left, bottom, up is distance 1
        First, we create a queue with all lands.
        Using BFS, exhaust all lands and populate queue with one level distance water cells.
        So, next round, we have queue with all water cells which are one level away from lands.
        We mark these waters as lands and keep doing this iteration.
        We count the iteration and that would be the final answer(iteration continues untill the queue is empty)
        """
        m, n = len(grid), len(grid[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m*n or len(q)==0: 
            return -1
        iteration = 0
        while q:
            iteration = iteration + 1
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in ([0,1],[0,-1],[1,0],[-1,0]):
                    new_x, new_y = x+dx, y+dy
                    if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 1
                        
        return iteration-1
                    
                
        
        