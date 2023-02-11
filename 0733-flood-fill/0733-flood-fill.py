from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m,n = len(image), len(image[0])
        q, visited, initial_color = deque(), set(), image[sr][sc]
        
        if initial_color == color:
            return image
        
        image[sr][sc] = color
        
        q.append([sr, sc])
        visited.add((sr,sc))
        
        while q:
            x,y = q.popleft()
            for dx, dy in [[0,1], [0,-1],[1,0],[-1,0]]:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<m and 0<=new_y<n:
                    if (new_x, new_y) not in visited:
                        if image[new_x][new_y] == initial_color:
                            image[new_x][new_y] = color
                            visited.add((new_x,new_y))
                            q.append([new_x, new_y])
                            
        return image
                            
        
        