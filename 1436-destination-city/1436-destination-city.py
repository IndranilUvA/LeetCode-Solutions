class Solution:
    
    """
    Since the graph is forming a line without a loop, we create a graph with source as keys and 
    destinations as values. Now, we loop through destinations/ values and check if that was ever a key/source. If not that is the answer.
    """
    
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        for u,v in paths:
            graph[u] = v
            
        for k,v in graph.items():
            if v not in graph:
                return v
            
        
        