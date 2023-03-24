from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        connections = set(((u,v) for u,v in connections))
        ## searching within set would be faster ##
        
        ## First, we create a undirected graph as usual ##
        graph = {}
        for u,v in connections:
            if u in graph:
                graph[u].append(v)
            if u not in graph:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            if v not in graph:
                graph[v] = [u]
                
        q = deque([0])
        visited = set([0])
        ans = 0
        
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    if (node,nei) in connections: ## First example - We only count if the [node,nei] is in connection, for example [0,1], that should be changed and that's why we count and move to node 1, anyway if that'snot the visited would have 4 and we count from there too 
                        ans = ans + 1
                    visited.add(nei)
                    q.append(nei)
        return ans
        