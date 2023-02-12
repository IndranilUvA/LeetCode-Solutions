from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        areas = []
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited: 
                    ans = 1
                    visited.add((i,j))
                    q = deque()
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        for dx,dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                            new_x,new_y = x+dx, y+dy
                            if 0<=new_x<m and 0<=new_y<n:
                                if (new_x,new_y) not in visited and grid[new_x][new_y] == 1:
                                    ans = ans + 1
                                    visited.add((new_x,new_y))
                                    q.append((new_x,new_y))
                
                areas.append(ans)    
                
        return max(areas)
                    
        