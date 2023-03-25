from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = n
        
        global_seen = set()
        
        for i in range(n):
            if i not in global_seen:
                global_seen.add(i)
                seen = set([i])
                q = deque([i])
                while q:
                    node = q.popleft()
                    for j in range(n):
                        if j!=node and isConnected[node][j]==1:
                            if j not in seen:
                                seen.add(j)
                                q.append(j)
                                global_seen.add(j)

                ans = ans - (len(seen)-1)
        
        return ans
        