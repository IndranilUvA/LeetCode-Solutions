from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = {}, {}
        
        for i,j in redEdges:
            if i in red:
                red[i].append(j)
            else:
                red[i] = [j]
        for i,j in blueEdges:
            if i in blue:
                blue[i].append(j)
            else:
                blue[i] = [j]
                
        q, visited, ans= deque(), set(), [-1]*n
        q.append([0,0,"None"])
        visited.add((0,"None"))
        
        while q:
            node, dist, color = q.popleft()
            if ans[node] == -1:
                ans[node] = dist
            
            if color!="Red" and node in red:
                for ne in red[node]:
                    if (ne, "Red") not in visited:
                        visited.add((ne, "Red"))
                        q.append([ne, dist+1, "Red"])
            
            if color!="Blue" and node in blue:
                for ne in blue[node]:
                    if (ne, "Blue") not in visited:
                        visited.add((ne, "Blue"))
                        q.append([ne, dist+1, "Blue"])
            
        return ans
    