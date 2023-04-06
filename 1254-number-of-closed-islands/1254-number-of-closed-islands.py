from collections import deque
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        seen = set()
        if m <=1 or n<=1:
            return 0
        def bfs(i,j):
            """
            Run BFS on lands only
            If i,j is part of closed island, return 1, else 0
            Also should incorporate all connecting lands into seen
            If the lands are in border then they are not part of closed island 
            """
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                return 0
            q = deque([[i,j]])
            connected = True
            while q:
                x,y = q.popleft()
                if x == 0 or y == 0 or x == m-1 or y == n-1:## checking if a land is in broder
                    connected = False
                for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                    next_x, next_y = x+dx, y+dy
                    if 0<=next_x<m and 0<=next_y<n and grid[next_x][next_y] == 0:
                        if (next_x, next_y) not in seen:
                            seen.add((next_x, next_y))
                            q.append([next_x, next_y])
            ## If we get out of while loop then it has travelled all lands in a closed islands
            return connected
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in seen:
                    if bfs(i,j):
                        ans = ans + 1
        return ans
                            
        
        