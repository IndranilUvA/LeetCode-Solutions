class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = {}
        for u,v in edges:
            if u in graph:
                graph[u].append(v)
            if u not in graph:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            if v not in graph:
                graph[v] = [u]
                
        num_nodes = len(graph)
        for k,v in graph.items():
            if len(v) == num_nodes - 1:
                return k
        